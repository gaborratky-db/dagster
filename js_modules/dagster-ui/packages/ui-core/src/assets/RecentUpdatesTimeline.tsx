import {
  Box,
  Caption,
  Colors,
  Icon,
  Popover,
  Spinner,
  Subtitle2,
  Tag,
  useViewport,
} from '@dagster-io/ui-components';
import {useMemo} from 'react';
import {Link} from 'react-router-dom';
import styled from 'styled-components';

import {RunlessEventTag} from './RunlessEventTag';
import {assetDetailsPathForKey} from './assetDetailsPathForKey';
import {isRunlessEvent} from './isRunlessEvent';
import {AssetKey} from './types';
import {useRecentAssetEvents} from './useRecentAssetEvents';
import {Timestamp} from '../app/time/Timestamp';
import {AssetRunLink} from '../asset-graph/AssetRunLinking';
import {RunStatusWithStats} from '../runs/RunStatusDots';
import {titleForRun} from '../runs/RunUtils';
import {useFormatDateTime} from '../ui/useFormatDateTime';

const MIN_TICK_WIDTH = 5;
const BUCKETS = 100;

export const RecentUpdatesTimeline = ({
  assetKey,
  materializations,
  loading,
}: {
  assetKey: AssetKey;
  materializations: ReturnType<typeof useRecentAssetEvents>['materializations'];
  loading: boolean;
}) => {
  const {containerProps, viewport} = useViewport();
  const widthAvailablePerTick = viewport.width / BUCKETS;

  const tickWidth = Math.max(widthAvailablePerTick, MIN_TICK_WIDTH);

  const buckets = Math.floor(viewport.width / tickWidth);

  const sortedMaterializations = useMemo(() => {
    return [...materializations].sort((a, b) => parseInt(a.timestamp) - parseInt(b.timestamp));
  }, [materializations]);

  const startTimestamp = parseInt(sortedMaterializations[0]?.timestamp ?? '0');
  const endTimestamp = parseInt(
    sortedMaterializations[sortedMaterializations.length - 1]?.timestamp ?? '0',
  );
  const timeRange = endTimestamp - startTimestamp;
  const bucketTimeRange = timeRange / buckets;

  const bucketedMaterializations = useMemo(() => {
    if (!viewport.width) {
      return [];
    }
    const firstPassBucketsArray: Array<{
      index: number;
      materializations: typeof materializations;
    }> = new Array(buckets);

    sortedMaterializations.forEach((materialization) => {
      const bucketIndex = Math.min(
        Math.floor((parseInt(materialization.timestamp) - startTimestamp) / bucketTimeRange),
        buckets - 1,
      );
      firstPassBucketsArray[bucketIndex] = firstPassBucketsArray[bucketIndex] || {
        index: bucketIndex,
        materializations: [] as typeof materializations,
      };
      firstPassBucketsArray[bucketIndex]!.materializations.push(materialization);
    });

    const secondPassBucketsArray: Array<{
      start: number;
      end: number;
      materializations: typeof materializations;
    }> = [];

    firstPassBucketsArray.forEach((bucket) => {
      const lastBucket = secondPassBucketsArray[secondPassBucketsArray.length - 1];
      if (!lastBucket || lastBucket.end !== bucket.index) {
        secondPassBucketsArray.push({
          start: bucket.index,
          end: bucket.index + 1,
          materializations: bucket.materializations,
        });
      } else {
        lastBucket.end = bucket.index + 1;
        lastBucket.materializations = [...lastBucket.materializations, ...bucket.materializations];
      }
    });

    return secondPassBucketsArray;
  }, [viewport.width, buckets, sortedMaterializations, startTimestamp, bucketTimeRange]);

  const formatDateTime = useFormatDateTime();

  if (loading) {
    return (
      <Box flex={{direction: 'row', alignItems: 'center', gap: 8}}>
        <Subtitle2>Recent updates</Subtitle2>
        <Spinner purpose="body-text" />
      </Box>
    );
  }

  if (!materializations.length) {
    return (
      <Box flex={{direction: 'row', alignItems: 'center', gap: 8}}>
        <Subtitle2>Recent updates</Subtitle2>
        <Caption color={Colors.textLight()}>No materialization events found</Caption>
      </Box>
    );
  }

  return (
    <Box flex={{direction: 'column', gap: 4}}>
      <Box flex={{direction: 'row', justifyContent: 'space-between'}}>
        <Subtitle2>Recent updates</Subtitle2>
        <Caption color={Colors.textLighter()}>
          {materializations.length === 100
            ? 'Last 100 updates'
            : `Showing all ${materializations.length} updates`}
        </Caption>
      </Box>
      <Box border="all" padding={6 as any} style={{height: 32, overflow: 'hidden'}}>
        <div {...containerProps} style={{width: '100%', height: 20, position: 'relative'}}>
          {bucketedMaterializations.map((bucket) => {
            const width = bucket.end - bucket.start;
            return (
              <>
                <TickWrapper
                  key={bucket.start}
                  style={{
                    left: (100 * bucket.start) / buckets + '%',
                    width: (100 * width) / buckets + '%',
                  }}
                >
                  <Popover
                    content={
                      <Box flex={{direction: 'column', gap: 8}}>
                        <Box padding={8} border="bottom">
                          <Subtitle2>Materializations</Subtitle2>
                        </Box>
                        <div style={{maxHeight: 'min(80vh, 300px)', overflow: 'scroll'}}>
                          {bucket.materializations
                            .sort((a, b) => parseInt(b.timestamp) - parseInt(a.timestamp))
                            .map((materialization, index) => (
                              <AssetUpdate
                                assetKey={assetKey}
                                event={materialization}
                                key={index}
                              />
                            ))}
                        </div>
                      </Box>
                    }
                  >
                    <>
                      <Tick>
                        {bucket.materializations.map(({timestamp}) => {
                          const bucketStartTime = startTimestamp + bucket.start * bucketTimeRange;
                          const bucketEndTimestamp = startTimestamp + bucket.end * bucketTimeRange;
                          const bucketRange = bucketEndTimestamp - bucketStartTime;
                          const percent =
                            (100 * (parseInt(timestamp) - bucketStartTime)) / bucketRange;

                          return (
                            <InnerTick
                              key={timestamp}
                              style={{
                                left: `min(calc(100% - 1px), ${percent}%`,
                              }}
                            />
                          );
                        })}
                        <TickText>
                          {bucket.materializations.length > 1
                            ? bucket.materializations.length
                            : null}
                        </TickText>
                      </Tick>
                    </>
                  </Popover>
                </TickWrapper>
              </>
            );
          })}
        </div>
      </Box>
      <Box padding={{top: 4}} flex={{justifyContent: 'space-between'}}>
        <Caption color={Colors.textLighter()}>
          {formatDateTime(new Date(startTimestamp), {})}
        </Caption>
        <Caption color={Colors.textLighter()}>{formatDateTime(new Date(endTimestamp), {})}</Caption>
      </Box>
    </Box>
  );
};

const AssetUpdate = ({
  assetKey,
  event,
}: {
  assetKey: AssetKey;
  event: ReturnType<typeof useRecentAssetEvents>['materializations'][0];
}) => {
  const run = event?.runOrError.__typename === 'Run' ? event.runOrError : null;
  return (
    <Box padding={4} border="bottom" flex={{justifyContent: 'space-between', gap: 8}}>
      <Box flex={{gap: 4, direction: 'row', alignItems: 'center'}}>
        {event.__typename === 'MaterializationEvent' ? (
          <Icon name="materialization" />
        ) : (
          <Icon name="observation" />
        )}
        <Link
          to={assetDetailsPathForKey(assetKey, {
            view: 'events',
            time: event.timestamp,
          })}
        >
          <Caption>
            <Timestamp timestamp={{ms: Number(event.timestamp)}} />
          </Caption>
        </Link>
      </Box>
      <div>
        {event && run ? (
          <Tag>
            <AssetRunLink
              runId={run.id}
              assetKey={assetKey}
              event={{stepKey: event.stepKey, timestamp: event.timestamp}}
            >
              <Box flex={{gap: 4, direction: 'row', alignItems: 'center'}}>
                <RunStatusWithStats runId={run.id} status={run.status} size={8} />
                {titleForRun(run)}
              </Box>
            </AssetRunLink>
          </Tag>
        ) : event && isRunlessEvent(event) ? (
          <RunlessEventTag tags={event.tags} />
        ) : undefined}
      </div>
    </Box>
  );
};

const Tick = styled.div`
  position: absolute;
  width 100%;
  top: 0;
  bottom: 0;
  overflow: hidden;
  background-color: transparent;
  cursor: pointer;
  border-radius: 2px;
  &:hover {
    background-color: ${Colors.accentGreenHover()};
  }

`;

const TickText = styled.div`
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  display: grid;
  place-content: center;
  color: transparent;
  background: none;
  user-select: none;
  &:hover {
    user-select: initial;
    color: ${Colors.textLight()};
  }
`;

const TickWrapper = styled.div`
  position: absolute;
  height: 20px;
  * {
    height: 20px;
  }
`;

const InnerTick = styled.div`
  width: 1px;
  background-color: ${Colors.accentGreen()};
  top: 0;
  bottom: 0;
  position: absolute;
  opacity: 0.5;
  pointer-events: none;
`;
