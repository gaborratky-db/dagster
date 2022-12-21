/* tslint:disable */
/* eslint-disable */
// @generated
// This file was automatically generated and should not be edited.

import { BulkActionStatus } from "./../../types/globalTypes";

// ====================================================
// GraphQL fragment: BackfillTableFragment
// ====================================================

export interface BackfillTableFragment_partitionSet_repositoryOrigin {
  __typename: "RepositoryOrigin";
  id: string;
  repositoryName: string;
  repositoryLocationName: string;
}

export interface BackfillTableFragment_partitionSet {
  __typename: "PartitionSet";
  id: string;
  name: string;
  mode: string;
  pipelineName: string;
  repositoryOrigin: BackfillTableFragment_partitionSet_repositoryOrigin;
}

export interface BackfillTableFragment_assetSelection {
  __typename: "AssetKey";
  path: string[];
}

export interface BackfillTableFragment_error_causes {
  __typename: "PythonError";
  message: string;
  stack: string[];
}

export interface BackfillTableFragment_error {
  __typename: "PythonError";
  message: string;
  stack: string[];
  causes: BackfillTableFragment_error_causes[];
}

export interface BackfillTableFragment {
  __typename: "PartitionBackfill";
  backfillId: string;
  status: BulkActionStatus;
  numRequested: number;
  partitionNames: string[];
  numPartitions: number;
  timestamp: number;
  partitionSetName: string;
  partitionSet: BackfillTableFragment_partitionSet | null;
  assetSelection: BackfillTableFragment_assetSelection[] | null;
  error: BackfillTableFragment_error | null;
}
