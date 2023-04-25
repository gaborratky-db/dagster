// Generated GraphQL types, do not edit manually.

import * as Types from '../../graphql/types';

export type ConfigForRunQueryVariables = Types.Exact<{
  runId: Types.Scalars['ID'];
}>;

export type ConfigForRunQuery = {
  __typename: 'DagitQuery';
  runOrError:
    | {
        __typename: 'PythonError';
        message: string;
        stack: Array<string>;
        errorChain: Array<{
          __typename: 'ErrorChainLink';
          isExplicitLink: boolean;
          error: {__typename: 'PythonError'; message: string; stack: Array<string>};
        }>;
      }
    | {
        __typename: 'Run';
        id: string;
        mode: string | null;
        runConfigYaml: string;
        solidSelection: Array<string> | null;
      }
    | {__typename: 'RunNotFoundError'};
};
