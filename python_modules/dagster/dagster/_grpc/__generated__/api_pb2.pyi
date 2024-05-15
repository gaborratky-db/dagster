"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
If you make changes to this file, run "python -m dagster._grpc.compile" after."""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Empty(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Empty = Empty

@typing_extensions.final
class PingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ECHO_FIELD_NUMBER: builtins.int
    echo: builtins.str
    def __init__(
        self,
        *,
        echo: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["echo", b"echo"]) -> None: ...

global___PingRequest = PingRequest

@typing_extensions.final
class PingReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ECHO_FIELD_NUMBER: builtins.int
    SERIALIZED_SERVER_UTILIZATION_METRICS_FIELD_NUMBER: builtins.int
    echo: builtins.str
    serialized_server_utilization_metrics: builtins.str
    def __init__(
        self,
        *,
        echo: builtins.str = ...,
        serialized_server_utilization_metrics: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "echo",
            b"echo",
            "serialized_server_utilization_metrics",
            b"serialized_server_utilization_metrics",
        ],
    ) -> None: ...

global___PingReply = PingReply

@typing_extensions.final
class StreamingPingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEQUENCE_LENGTH_FIELD_NUMBER: builtins.int
    ECHO_FIELD_NUMBER: builtins.int
    sequence_length: builtins.int
    echo: builtins.str
    def __init__(
        self,
        *,
        sequence_length: builtins.int = ...,
        echo: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "echo", b"echo", "sequence_length", b"sequence_length"
        ],
    ) -> None: ...

global___StreamingPingRequest = StreamingPingRequest

@typing_extensions.final
class StreamingPingEvent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEQUENCE_NUMBER_FIELD_NUMBER: builtins.int
    ECHO_FIELD_NUMBER: builtins.int
    sequence_number: builtins.int
    echo: builtins.str
    def __init__(
        self,
        *,
        sequence_number: builtins.int = ...,
        echo: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "echo", b"echo", "sequence_number", b"sequence_number"
        ],
    ) -> None: ...

global___StreamingPingEvent = StreamingPingEvent

@typing_extensions.final
class GetServerIdReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["server_id", b"server_id"]
    ) -> None: ...

global___GetServerIdReply = GetServerIdReply

@typing_extensions.final
class ExecutionPlanSnapshotRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXECUTION_PLAN_SNAPSHOT_ARGS_FIELD_NUMBER: builtins.int
    serialized_execution_plan_snapshot_args: builtins.str
    def __init__(
        self,
        *,
        serialized_execution_plan_snapshot_args: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_execution_plan_snapshot_args", b"serialized_execution_plan_snapshot_args"
        ],
    ) -> None: ...

global___ExecutionPlanSnapshotRequest = ExecutionPlanSnapshotRequest

@typing_extensions.final
class ExecutionPlanSnapshotReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXECUTION_PLAN_SNAPSHOT_FIELD_NUMBER: builtins.int
    serialized_execution_plan_snapshot: builtins.str
    def __init__(
        self,
        *,
        serialized_execution_plan_snapshot: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_execution_plan_snapshot", b"serialized_execution_plan_snapshot"
        ],
    ) -> None: ...

global___ExecutionPlanSnapshotReply = ExecutionPlanSnapshotReply

@typing_extensions.final
class ExternalPartitionNamesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_PARTITION_NAMES_ARGS_FIELD_NUMBER: builtins.int
    serialized_partition_names_args: builtins.str
    def __init__(
        self,
        *,
        serialized_partition_names_args: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_partition_names_args", b"serialized_partition_names_args"
        ],
    ) -> None: ...

global___ExternalPartitionNamesRequest = ExternalPartitionNamesRequest

@typing_extensions.final
class ExternalPartitionNamesReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXTERNAL_PARTITION_NAMES_OR_EXTERNAL_PARTITION_EXECUTION_ERROR_FIELD_NUMBER: (
        builtins.int
    )
    serialized_external_partition_names_or_external_partition_execution_error: builtins.str
    def __init__(
        self,
        *,
        serialized_external_partition_names_or_external_partition_execution_error: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_external_partition_names_or_external_partition_execution_error",
            b"serialized_external_partition_names_or_external_partition_execution_error",
        ],
    ) -> None: ...

global___ExternalPartitionNamesReply = ExternalPartitionNamesReply

@typing_extensions.final
class ExternalNotebookDataRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTEBOOK_PATH_FIELD_NUMBER: builtins.int
    notebook_path: builtins.str
    def __init__(
        self,
        *,
        notebook_path: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["notebook_path", b"notebook_path"]
    ) -> None: ...

global___ExternalNotebookDataRequest = ExternalNotebookDataRequest

@typing_extensions.final
class ExternalNotebookDataReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENT_FIELD_NUMBER: builtins.int
    content: builtins.bytes
    def __init__(
        self,
        *,
        content: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content", b"content"]) -> None: ...

global___ExternalNotebookDataReply = ExternalNotebookDataReply

@typing_extensions.final
class ExternalPartitionConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_PARTITION_ARGS_FIELD_NUMBER: builtins.int
    serialized_partition_args: builtins.str
    def __init__(
        self,
        *,
        serialized_partition_args: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_partition_args", b"serialized_partition_args"
        ],
    ) -> None: ...

global___ExternalPartitionConfigRequest = ExternalPartitionConfigRequest

@typing_extensions.final
class ExternalPartitionConfigReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXTERNAL_PARTITION_CONFIG_OR_EXTERNAL_PARTITION_EXECUTION_ERROR_FIELD_NUMBER: (
        builtins.int
    )
    serialized_external_partition_config_or_external_partition_execution_error: builtins.str
    def __init__(
        self,
        *,
        serialized_external_partition_config_or_external_partition_execution_error: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_external_partition_config_or_external_partition_execution_error",
            b"serialized_external_partition_config_or_external_partition_execution_error",
        ],
    ) -> None: ...

global___ExternalPartitionConfigReply = ExternalPartitionConfigReply

@typing_extensions.final
class ExternalPartitionTagsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_PARTITION_ARGS_FIELD_NUMBER: builtins.int
    serialized_partition_args: builtins.str
    def __init__(
        self,
        *,
        serialized_partition_args: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_partition_args", b"serialized_partition_args"
        ],
    ) -> None: ...

global___ExternalPartitionTagsRequest = ExternalPartitionTagsRequest

@typing_extensions.final
class ExternalPartitionTagsReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXTERNAL_PARTITION_TAGS_OR_EXTERNAL_PARTITION_EXECUTION_ERROR_FIELD_NUMBER: (
        builtins.int
    )
    serialized_external_partition_tags_or_external_partition_execution_error: builtins.str
    def __init__(
        self,
        *,
        serialized_external_partition_tags_or_external_partition_execution_error: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_external_partition_tags_or_external_partition_execution_error",
            b"serialized_external_partition_tags_or_external_partition_execution_error",
        ],
    ) -> None: ...

global___ExternalPartitionTagsReply = ExternalPartitionTagsReply

@typing_extensions.final
class ExternalPartitionSetExecutionParamsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_PARTITION_SET_EXECUTION_PARAM_ARGS_FIELD_NUMBER: builtins.int
    serialized_partition_set_execution_param_args: builtins.str
    def __init__(
        self,
        *,
        serialized_partition_set_execution_param_args: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_partition_set_execution_param_args",
            b"serialized_partition_set_execution_param_args",
        ],
    ) -> None: ...

global___ExternalPartitionSetExecutionParamsRequest = ExternalPartitionSetExecutionParamsRequest

@typing_extensions.final
class ListRepositoriesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ListRepositoriesRequest = ListRepositoriesRequest

@typing_extensions.final
class ListRepositoriesReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_LIST_REPOSITORIES_RESPONSE_OR_ERROR_FIELD_NUMBER: builtins.int
    serialized_list_repositories_response_or_error: builtins.str
    def __init__(
        self,
        *,
        serialized_list_repositories_response_or_error: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_list_repositories_response_or_error",
            b"serialized_list_repositories_response_or_error",
        ],
    ) -> None: ...

global___ListRepositoriesReply = ListRepositoriesReply

@typing_extensions.final
class ExternalPipelineSubsetSnapshotRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_PIPELINE_SUBSET_SNAPSHOT_ARGS_FIELD_NUMBER: builtins.int
    serialized_pipeline_subset_snapshot_args: builtins.str
    def __init__(
        self,
        *,
        serialized_pipeline_subset_snapshot_args: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_pipeline_subset_snapshot_args", b"serialized_pipeline_subset_snapshot_args"
        ],
    ) -> None: ...

global___ExternalPipelineSubsetSnapshotRequest = ExternalPipelineSubsetSnapshotRequest

@typing_extensions.final
class ExternalPipelineSubsetSnapshotReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXTERNAL_PIPELINE_SUBSET_RESULT_FIELD_NUMBER: builtins.int
    serialized_external_pipeline_subset_result: builtins.str
    def __init__(
        self,
        *,
        serialized_external_pipeline_subset_result: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_external_pipeline_subset_result",
            b"serialized_external_pipeline_subset_result",
        ],
    ) -> None: ...

global___ExternalPipelineSubsetSnapshotReply = ExternalPipelineSubsetSnapshotReply

@typing_extensions.final
class ExternalRepositoryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_REPOSITORY_PYTHON_ORIGIN_FIELD_NUMBER: builtins.int
    DEFER_SNAPSHOTS_FIELD_NUMBER: builtins.int
    serialized_repository_python_origin: builtins.str
    defer_snapshots: builtins.bool
    def __init__(
        self,
        *,
        serialized_repository_python_origin: builtins.str = ...,
        defer_snapshots: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "defer_snapshots",
            b"defer_snapshots",
            "serialized_repository_python_origin",
            b"serialized_repository_python_origin",
        ],
    ) -> None: ...

global___ExternalRepositoryRequest = ExternalRepositoryRequest

@typing_extensions.final
class ExternalRepositoryReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXTERNAL_REPOSITORY_DATA_FIELD_NUMBER: builtins.int
    serialized_external_repository_data: builtins.str
    def __init__(
        self,
        *,
        serialized_external_repository_data: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_external_repository_data", b"serialized_external_repository_data"
        ],
    ) -> None: ...

global___ExternalRepositoryReply = ExternalRepositoryReply

@typing_extensions.final
class StreamingExternalRepositoryEvent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEQUENCE_NUMBER_FIELD_NUMBER: builtins.int
    SERIALIZED_EXTERNAL_REPOSITORY_CHUNK_FIELD_NUMBER: builtins.int
    sequence_number: builtins.int
    serialized_external_repository_chunk: builtins.str
    def __init__(
        self,
        *,
        sequence_number: builtins.int = ...,
        serialized_external_repository_chunk: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "sequence_number",
            b"sequence_number",
            "serialized_external_repository_chunk",
            b"serialized_external_repository_chunk",
        ],
    ) -> None: ...

global___StreamingExternalRepositoryEvent = StreamingExternalRepositoryEvent

@typing_extensions.final
class ExternalScheduleExecutionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXTERNAL_SCHEDULE_EXECUTION_ARGS_FIELD_NUMBER: builtins.int
    serialized_external_schedule_execution_args: builtins.str
    def __init__(
        self,
        *,
        serialized_external_schedule_execution_args: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_external_schedule_execution_args",
            b"serialized_external_schedule_execution_args",
        ],
    ) -> None: ...

global___ExternalScheduleExecutionRequest = ExternalScheduleExecutionRequest

@typing_extensions.final
class ExternalSensorExecutionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXTERNAL_SENSOR_EXECUTION_ARGS_FIELD_NUMBER: builtins.int
    serialized_external_sensor_execution_args: builtins.str
    def __init__(
        self,
        *,
        serialized_external_sensor_execution_args: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_external_sensor_execution_args",
            b"serialized_external_sensor_execution_args",
        ],
    ) -> None: ...

global___ExternalSensorExecutionRequest = ExternalSensorExecutionRequest

@typing_extensions.final
class ExternalConditionEvaluationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXTERNAL_CONDITION_EVALUATION_ARGS_FIELD_NUMBER: builtins.int
    serialized_external_condition_evaluation_args: builtins.str
    def __init__(
        self,
        *,
        serialized_external_condition_evaluation_args: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_external_condition_evaluation_args",
            b"serialized_external_condition_evaluation_args",
        ],
    ) -> None: ...

global___ExternalConditionEvaluationRequest = ExternalConditionEvaluationRequest

@typing_extensions.final
class ExternalConditionEvaluationReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_CONDITION_EVALUATION_FIELD_NUMBER: builtins.int
    serialized_condition_evaluation: builtins.str
    def __init__(
        self,
        *,
        serialized_condition_evaluation: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_condition_evaluation", b"serialized_condition_evaluation"
        ],
    ) -> None: ...

global___ExternalConditionEvaluationReply = ExternalConditionEvaluationReply

@typing_extensions.final
class StreamingChunkEvent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEQUENCE_NUMBER_FIELD_NUMBER: builtins.int
    SERIALIZED_CHUNK_FIELD_NUMBER: builtins.int
    sequence_number: builtins.int
    serialized_chunk: builtins.str
    def __init__(
        self,
        *,
        sequence_number: builtins.int = ...,
        serialized_chunk: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "sequence_number", b"sequence_number", "serialized_chunk", b"serialized_chunk"
        ],
    ) -> None: ...

global___StreamingChunkEvent = StreamingChunkEvent

@typing_extensions.final
class ShutdownServerReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_SHUTDOWN_SERVER_RESULT_FIELD_NUMBER: builtins.int
    serialized_shutdown_server_result: builtins.str
    def __init__(
        self,
        *,
        serialized_shutdown_server_result: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_shutdown_server_result", b"serialized_shutdown_server_result"
        ],
    ) -> None: ...

global___ShutdownServerReply = ShutdownServerReply

@typing_extensions.final
class CancelExecutionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_CANCEL_EXECUTION_REQUEST_FIELD_NUMBER: builtins.int
    serialized_cancel_execution_request: builtins.str
    def __init__(
        self,
        *,
        serialized_cancel_execution_request: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_cancel_execution_request", b"serialized_cancel_execution_request"
        ],
    ) -> None: ...

global___CancelExecutionRequest = CancelExecutionRequest

@typing_extensions.final
class CancelExecutionReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_CANCEL_EXECUTION_RESULT_FIELD_NUMBER: builtins.int
    serialized_cancel_execution_result: builtins.str
    def __init__(
        self,
        *,
        serialized_cancel_execution_result: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_cancel_execution_result", b"serialized_cancel_execution_result"
        ],
    ) -> None: ...

global___CancelExecutionReply = CancelExecutionReply

@typing_extensions.final
class CanCancelExecutionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_CAN_CANCEL_EXECUTION_REQUEST_FIELD_NUMBER: builtins.int
    serialized_can_cancel_execution_request: builtins.str
    def __init__(
        self,
        *,
        serialized_can_cancel_execution_request: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_can_cancel_execution_request", b"serialized_can_cancel_execution_request"
        ],
    ) -> None: ...

global___CanCancelExecutionRequest = CanCancelExecutionRequest

@typing_extensions.final
class CanCancelExecutionReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_CAN_CANCEL_EXECUTION_RESULT_FIELD_NUMBER: builtins.int
    serialized_can_cancel_execution_result: builtins.str
    def __init__(
        self,
        *,
        serialized_can_cancel_execution_result: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_can_cancel_execution_result", b"serialized_can_cancel_execution_result"
        ],
    ) -> None: ...

global___CanCancelExecutionReply = CanCancelExecutionReply

@typing_extensions.final
class StartRunRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_EXECUTE_RUN_ARGS_FIELD_NUMBER: builtins.int
    serialized_execute_run_args: builtins.str
    def __init__(
        self,
        *,
        serialized_execute_run_args: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_execute_run_args", b"serialized_execute_run_args"
        ],
    ) -> None: ...

global___StartRunRequest = StartRunRequest

@typing_extensions.final
class StartRunReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_START_RUN_RESULT_FIELD_NUMBER: builtins.int
    serialized_start_run_result: builtins.str
    def __init__(
        self,
        *,
        serialized_start_run_result: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_start_run_result", b"serialized_start_run_result"
        ],
    ) -> None: ...

global___StartRunReply = StartRunReply

@typing_extensions.final
class GetCurrentImageReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_CURRENT_IMAGE_FIELD_NUMBER: builtins.int
    serialized_current_image: builtins.str
    def __init__(
        self,
        *,
        serialized_current_image: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_current_image", b"serialized_current_image"
        ],
    ) -> None: ...

global___GetCurrentImageReply = GetCurrentImageReply

@typing_extensions.final
class GetCurrentRunsReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_CURRENT_RUNS_FIELD_NUMBER: builtins.int
    serialized_current_runs: builtins.str
    def __init__(
        self,
        *,
        serialized_current_runs: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_current_runs", b"serialized_current_runs"
        ],
    ) -> None: ...

global___GetCurrentRunsReply = GetCurrentRunsReply

@typing_extensions.final
class ExternalJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_REPOSITORY_ORIGIN_FIELD_NUMBER: builtins.int
    JOB_NAME_FIELD_NUMBER: builtins.int
    serialized_repository_origin: builtins.str
    job_name: builtins.str
    def __init__(
        self,
        *,
        serialized_repository_origin: builtins.str = ...,
        job_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "job_name", b"job_name", "serialized_repository_origin", b"serialized_repository_origin"
        ],
    ) -> None: ...

global___ExternalJobRequest = ExternalJobRequest

@typing_extensions.final
class ExternalJobReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_JOB_DATA_FIELD_NUMBER: builtins.int
    SERIALIZED_ERROR_FIELD_NUMBER: builtins.int
    serialized_job_data: builtins.str
    serialized_error: builtins.str
    def __init__(
        self,
        *,
        serialized_job_data: builtins.str = ...,
        serialized_error: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_error", b"serialized_error", "serialized_job_data", b"serialized_job_data"
        ],
    ) -> None: ...

global___ExternalJobReply = ExternalJobReply

@typing_extensions.final
class ExternalScheduleExecutionReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_SCHEDULE_RESULT_FIELD_NUMBER: builtins.int
    serialized_schedule_result: builtins.str
    def __init__(
        self,
        *,
        serialized_schedule_result: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_schedule_result", b"serialized_schedule_result"
        ],
    ) -> None: ...

global___ExternalScheduleExecutionReply = ExternalScheduleExecutionReply

@typing_extensions.final
class ExternalSensorExecutionReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_SENSOR_RESULT_FIELD_NUMBER: builtins.int
    serialized_sensor_result: builtins.str
    def __init__(
        self,
        *,
        serialized_sensor_result: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "serialized_sensor_result", b"serialized_sensor_result"
        ],
    ) -> None: ...

global___ExternalSensorExecutionReply = ExternalSensorExecutionReply

@typing_extensions.final
class ReloadCodeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ReloadCodeRequest = ReloadCodeRequest

@typing_extensions.final
class ReloadCodeReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIALIZED_ERROR_FIELD_NUMBER: builtins.int
    serialized_error: builtins.str
    def __init__(
        self,
        *,
        serialized_error: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["serialized_error", b"serialized_error"]
    ) -> None: ...

global___ReloadCodeReply = ReloadCodeReply
