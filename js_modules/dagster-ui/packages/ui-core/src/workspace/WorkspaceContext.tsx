import {useApolloClient} from '@apollo/client';
import sortBy from 'lodash/sortBy';
import React, {useCallback, useContext, useEffect, useMemo, useRef, useState} from 'react';

import {CODE_LOCATION_STATUS_QUERY, LOCATION_WORKSPACE_QUERY} from './WorkspaceQueries';
import {buildRepoAddress} from './buildRepoAddress';
import {findRepoContainingPipeline} from './findRepoContainingPipeline';
import {RepoAddress} from './types';
import {
  CodeLocationStatusQuery,
  CodeLocationStatusQueryVariables,
  LocationWorkspaceQuery,
  LocationWorkspaceQueryVariables,
  WorkspaceLocationFragment,
  WorkspaceLocationNodeFragment,
  WorkspaceRepositoryFragment,
  WorkspaceScheduleFragment,
  WorkspaceSensorFragment,
} from './types/WorkspaceQueries.types';
import {AppContext} from '../app/AppContext';
import {useRefreshAtInterval} from '../app/QueryRefresh';
import {PythonErrorFragment} from '../app/types/PythonErrorFragment.types';
import {PipelineSelector} from '../graphql/types';
import {useStateWithStorage} from '../hooks/useStateWithStorage';
import {useUpdatingRef} from '../hooks/useUpdatingRef';
import {getCachedData, getData, useIndexedDBCachedQuery} from '../search/useIndexedDBCachedQuery';

const CODE_LOCATION_STATUS_QUERY_KEY = 'CodeLocationStatusQuery';
const CODE_LOCATION_STATUS_QUERY_VERSION = 3;
const LOCATION_WORKSPACE_QUERY_VERSION = 5;
type Repository = WorkspaceRepositoryFragment;
type RepositoryLocation = WorkspaceLocationFragment;

export type WorkspaceRepositorySensor = WorkspaceSensorFragment;
export type WorkspaceRepositorySchedule = WorkspaceScheduleFragment;
export type WorkspaceRepositoryLocationNode = WorkspaceLocationNodeFragment;

export interface DagsterRepoOption {
  repositoryLocation: RepositoryLocation;
  repository: Repository;
}

type SetVisibleOrHiddenFn = (repoAddresses: RepoAddress[]) => void;

type WorkspaceState = {
  loading: boolean;
  locationEntries: WorkspaceRepositoryLocationNode[];
  allRepos: DagsterRepoOption[];
  visibleRepos: DagsterRepoOption[];
  data: Record<string, WorkspaceLocationNodeFragment | PythonErrorFragment>;
  refetch: () => Promise<LocationWorkspaceQuery[]>;

  toggleVisible: SetVisibleOrHiddenFn;
  setVisible: SetVisibleOrHiddenFn;
  setHidden: SetVisibleOrHiddenFn;
};

export const WorkspaceContext = React.createContext<WorkspaceState>(
  new Error('WorkspaceContext should never be uninitialized') as any,
);

export const HIDDEN_REPO_KEYS = 'dagster.hidden-repo-keys';

export const WorkspaceProvider = ({children}: {children: React.ReactNode}) => {
  const {localCacheIdPrefix} = useContext(AppContext);
  const codeLocationStatusQueryResult = useIndexedDBCachedQuery<
    CodeLocationStatusQuery,
    CodeLocationStatusQueryVariables
  >({
    query: CODE_LOCATION_STATUS_QUERY,
    version: CODE_LOCATION_STATUS_QUERY_VERSION,
    key: `${localCacheIdPrefix}/${CODE_LOCATION_STATUS_QUERY_KEY}`,
  });
  const fetch = codeLocationStatusQueryResult.fetch;
  useRefreshAtInterval({
    refresh: useCallback(async () => {
      return await fetch();
    }, [fetch]),
    intervalMs: 5000,
    leading: true,
  });

  const {data} = codeLocationStatusQueryResult;

  const locations = useMemo(() => getLocations(data), [data]);
  const prevLocations = useRef<typeof locations>({});

  const didInitiateFetchFromCache = useRef(false);
  const [didLoadCachedData, setDidLoadCachedData] = useState(false);

  const [locationsData, setLocationsData] = React.useState<
    Record<string, WorkspaceLocationNodeFragment | PythonErrorFragment>
  >({});

  useEffect(() => {
    // Load data from the cache
    if (didInitiateFetchFromCache.current) {
      return;
    }
    didInitiateFetchFromCache.current = true;
    (async () => {
      const data = await getCachedData<CodeLocationStatusQuery>({
        key: `${localCacheIdPrefix}/${CODE_LOCATION_STATUS_QUERY_KEY}`,
        version: CODE_LOCATION_STATUS_QUERY_VERSION,
      });
      const cachedLocations = getLocations(data);
      const prevCachedLocations: typeof locations = {};

      await Promise.all([
        ...Object.values(cachedLocations).map(async (location) => {
          const locationData = await getCachedData<LocationWorkspaceQuery>({
            key: `${localCacheIdPrefix}/${locationWorkspaceKey(location.name)}`,
            version: LOCATION_WORKSPACE_QUERY_VERSION,
          });
          const entry = locationData?.workspaceLocationEntryOrError;

          if (!entry) {
            return;
          }
          setLocationsData((locationsData) =>
            Object.assign({}, locationsData, {
              [location.name]: entry,
            }),
          );

          if (entry.__typename === 'WorkspaceLocationEntry') {
            prevCachedLocations[location.name] = location;
          }
        }),
      ]);
      prevLocations.current = prevCachedLocations;
      setDidLoadCachedData(true);
    })();
  }, [localCacheIdPrefix, locations]);

  const client = useApolloClient();

  const refetchLocation = useCallback(
    async (name: string) => {
      const locationData = await getData<LocationWorkspaceQuery, LocationWorkspaceQueryVariables>({
        client,
        query: LOCATION_WORKSPACE_QUERY,
        key: `${localCacheIdPrefix}/${locationWorkspaceKey(name)}`,
        version: LOCATION_WORKSPACE_QUERY_VERSION,
        variables: {
          name,
        },
        bypassCache: true,
      });
      const entry = locationData?.workspaceLocationEntryOrError;
      setLocationsData((locationsData) =>
        Object.assign({}, locationsData, {
          [name]: entry,
        }),
      );
      return locationData;
    },
    [client, localCacheIdPrefix],
  );

  const locationsToFetch = useMemo(() => {
    if (!didLoadCachedData) {
      return [];
    }
    const toFetch = Object.values(locations).filter((loc) => {
      const prev = prevLocations.current?.[loc.name];
      return prev?.updateTimestamp !== loc.updateTimestamp || prev?.loadStatus !== loc.loadStatus;
    });
    prevLocations.current = locations;
    return toFetch;
  }, [locations, didLoadCachedData]);

  useEffect(() => {
    locationsToFetch.forEach(async (location) => {
      refetchLocation(location.name);
    });
  }, [refetchLocation, locationsToFetch]);

  const locationsRemoved = useMemo(() => {
    return Object.values(prevLocations.current).filter((loc) => !locations[loc.name]);
  }, [locations]);

  useEffect(() => {
    if (locationsRemoved.length) {
      setLocationsData((locationsData) => {
        const copy = {...locationsData};
        locationsRemoved.forEach((loc) => {
          delete copy[loc.name];
          indexedDB.deleteDatabase(`${localCacheIdPrefix}/${locationWorkspaceKey(loc.name)}`);
        });
        return copy;
      });
    }
  }, [localCacheIdPrefix, locationsRemoved]);

  const locationEntries = useMemo(
    () =>
      Object.values(locationsData).filter(
        (entry): entry is WorkspaceLocationNodeFragment =>
          entry.__typename === 'WorkspaceLocationEntry',
      ),
    [locationsData],
  );

  const {allRepos} = React.useMemo(() => {
    let allRepos: DagsterRepoOption[] = [];

    allRepos = sortBy(
      locationEntries.reduce((accum, locationEntry) => {
        if (locationEntry.locationOrLoadError?.__typename !== 'RepositoryLocation') {
          return accum;
        }
        const repositoryLocation = locationEntry.locationOrLoadError;
        const reposForLocation = repositoryLocation.repositories.map((repository) => {
          return {repository, repositoryLocation};
        });
        return [...accum, ...reposForLocation];
      }, [] as DagsterRepoOption[]),

      // Sort by repo location, then by repo
      (r) => `${r.repositoryLocation.name}:${r.repository.name}`,
    );

    return {allRepos};
  }, [locationEntries]);

  const {visibleRepos, toggleVisible, setVisible, setHidden} = useVisibleRepos(allRepos);

  const locationsRef = useUpdatingRef(locations);

  const refetch = useCallback(async () => {
    return await Promise.all(
      Object.values(locationsRef.current).map((location) => refetchLocation(location.name)),
    );
  }, [locationsRef, refetchLocation]);

  return (
    <WorkspaceContext.Provider
      value={{
        loading: Object.keys(locationsData).length !== Object.keys(locations).length, // Only "loading" on initial load.
        locationEntries,
        allRepos,
        visibleRepos,
        toggleVisible,
        setVisible,
        setHidden,

        data: locationsData,
        refetch,
      }}
    >
      {children}
    </WorkspaceContext.Provider>
  );
};

function getLocations(d: CodeLocationStatusQuery | undefined | null) {
  const locations =
    d?.locationStatusesOrError?.__typename === 'WorkspaceLocationStatusEntries'
      ? d?.locationStatusesOrError.entries
      : [];
  return locations.reduce(
    (accum, loc) => {
      accum[loc.name] = loc;
      return accum;
    },
    {} as Record<string, (typeof locations)[0]>,
  );
}

function locationWorkspaceKey(name: string) {
  return `LocationWorkspace/${name}`;
}

/**
 * useVisibleRepos returns `{reposForKeys, toggleVisible, setVisible, setHidden}` and internally
 * mirrors the current selection into localStorage so that the default selection in new browser
 * windows is the repo currently active in your session.
 */
const validateHiddenKeys = (parsed: unknown) => (Array.isArray(parsed) ? parsed : []);

const useVisibleRepos = (
  allRepos: DagsterRepoOption[],
): {
  visibleRepos: DagsterRepoOption[];
  toggleVisible: SetVisibleOrHiddenFn;
  setVisible: SetVisibleOrHiddenFn;
  setHidden: SetVisibleOrHiddenFn;
} => {
  const {basePath} = React.useContext(AppContext);

  const [oldHiddenKeys, setOldHiddenKeys] = useStateWithStorage<string[]>(
    HIDDEN_REPO_KEYS,
    validateHiddenKeys,
  );
  const [hiddenKeys, setHiddenKeys] = useStateWithStorage<string[]>(
    basePath + ':' + HIDDEN_REPO_KEYS,
    validateHiddenKeys,
  );

  const hiddenKeysJSON = JSON.stringify([...hiddenKeys.sort()]);

  // TODO: Remove this logic eventually...
  const migratedOldHiddenKeys = React.useRef(false);
  if (oldHiddenKeys.length && !migratedOldHiddenKeys.current) {
    setHiddenKeys(oldHiddenKeys);
    setOldHiddenKeys(undefined);
    migratedOldHiddenKeys.current = true;
  }

  const toggleVisible = React.useCallback(
    (repoAddresses: RepoAddress[]) => {
      repoAddresses.forEach((repoAddress) => {
        const key = `${repoAddress.name}:${repoAddress.location}`;

        setHiddenKeys((current) => {
          let nextHiddenKeys = [...(current || [])];
          if (nextHiddenKeys.includes(key)) {
            nextHiddenKeys = nextHiddenKeys.filter((k) => k !== key);
          } else {
            nextHiddenKeys = [...nextHiddenKeys, key];
          }
          return nextHiddenKeys;
        });
      });
    },
    [setHiddenKeys],
  );

  const setVisible = React.useCallback(
    (repoAddresses: RepoAddress[]) => {
      const keysToShow = new Set(
        repoAddresses.map((repoAddress) => `${repoAddress.name}:${repoAddress.location}`),
      );
      setHiddenKeys((current) => {
        return current?.filter((key) => !keysToShow.has(key));
      });
    },
    [setHiddenKeys],
  );

  const setHidden = React.useCallback(
    (repoAddresses: RepoAddress[]) => {
      const keysToHide = new Set(
        repoAddresses.map((repoAddress) => `${repoAddress.name}:${repoAddress.location}`),
      );
      setHiddenKeys((current) => {
        const updatedSet = new Set([...(current || []), ...keysToHide]);
        return Array.from(updatedSet);
      });
    },
    [setHiddenKeys],
  );

  const visibleRepos = React.useMemo(() => {
    // If there's only one repo, skip the local storage check -- we have to show this one.
    if (allRepos.length === 1) {
      return allRepos;
    }
    const hiddenKeys = new Set(JSON.parse(hiddenKeysJSON));
    return allRepos.filter((o) => !hiddenKeys.has(getRepositoryOptionHash(o)));
  }, [allRepos, hiddenKeysJSON]);

  return {visibleRepos, toggleVisible, setVisible, setHidden};
};

// Public

const getRepositoryOptionHash = (a: DagsterRepoOption) =>
  `${a.repository.name}:${a.repositoryLocation.name}`;
export const useRepositoryOptions = () => {
  const {allRepos: options, loading} = React.useContext(WorkspaceContext);
  return {options, loading};
};

export const useRepository = (repoAddress: RepoAddress | null) => {
  const {options} = useRepositoryOptions();
  return findRepositoryAmongOptions(options, repoAddress) || null;
};

export const findRepositoryAmongOptions = (
  options: DagsterRepoOption[],
  repoAddress: RepoAddress | null,
) => {
  return repoAddress
    ? options.find(
        (option) =>
          option.repository.name === repoAddress.name &&
          option.repositoryLocation.name === repoAddress.location,
      )
    : null;
};

export const useActivePipelineForName = (pipelineName: string, snapshotId?: string) => {
  const {options} = useRepositoryOptions();
  const reposWithMatch = findRepoContainingPipeline(options, pipelineName, snapshotId);
  if (reposWithMatch[0]) {
    const match = reposWithMatch[0];
    return match.repository.pipelines.find((pipeline) => pipeline.name === pipelineName) || null;
  }
  return null;
};

export const getFeatureFlagForCodeLocation = (
  locationEntries: WorkspaceLocationNodeFragment[],
  locationName: string,
  flagName: string,
) => {
  const matchingLocation = locationEntries.find(({id}) => id === locationName);
  if (matchingLocation) {
    const {featureFlags} = matchingLocation;
    const matchingFlag = featureFlags.find(({name}) => name === flagName);
    if (matchingFlag) {
      return matchingFlag.enabled;
    }
  }
  return false;
};

export const useFeatureFlagForCodeLocation = (locationName: string, flagName: string) => {
  const {locationEntries} = useContext(WorkspaceContext);
  return getFeatureFlagForCodeLocation(locationEntries, locationName, flagName);
};

export const isThisThingAJob = (repo: DagsterRepoOption | null, pipelineOrJobName: string) => {
  const pipelineOrJob = repo?.repository.pipelines.find(
    (pipelineOrJob) => pipelineOrJob.name === pipelineOrJobName,
  );
  return !!pipelineOrJob?.isJob;
};

export const isThisThingAnAssetJob = (
  repo: DagsterRepoOption | null,
  pipelineOrJobName: string,
) => {
  const pipelineOrJob = repo?.repository.pipelines.find(
    (pipelineOrJob) => pipelineOrJob.name === pipelineOrJobName,
  );
  return !!pipelineOrJob?.isAssetJob;
};

export const buildPipelineSelector = (
  repoAddress: RepoAddress | null,
  pipelineName: string,
  solidSelection?: string[],
) => {
  const repositorySelector = {
    repositoryName: repoAddress?.name || '',
    repositoryLocationName: repoAddress?.location || '',
  };

  return {
    ...repositorySelector,
    pipelineName,
    solidSelection,
  } as PipelineSelector;
};

export const optionToRepoAddress = (option: DagsterRepoOption) =>
  buildRepoAddress(option.repository.name, option.repository.location.name);
