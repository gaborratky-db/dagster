from typing import Any, Dict

from dagster import (
    AssetKey,
    DailyPartitionsDefinition,
)
from dagster._core.definitions.asset_check_factories.utils import (
    DEADLINE_CRON_PARAM_KEY,
    FRESHNESS_PARAMS_METADATA_KEY,
    LOWER_BOUND_DELTA_PARAM_KEY,
    TIMEZONE_PARAM_KEY,
)
from dagster._core.definitions.asset_check_spec import AssetCheckKey
from dagster._core.definitions.metadata.metadata_value import JsonMetadataValue
from dagster._seven.compat import pendulum
from dagster_dbt.asset_decorator import dbt_assets
from dagster_dbt.freshness_builder import build_freshness_checks_from_dbt_assets


def test_dbt_last_update_freshness_checks(
    test_last_update_freshness_manifest: Dict[str, Any],
) -> None:
    @dbt_assets(manifest=test_last_update_freshness_manifest)
    def my_dbt_assets(): ...

    freshness_checks = build_freshness_checks_from_dbt_assets([my_dbt_assets])
    # We added a freshness check to the customers table only.
    assert len(freshness_checks) == 1
    freshness_check = freshness_checks[0]
    assert list(freshness_check.check_keys)[0] == AssetCheckKey(  # noqa
        AssetKey("customers"), "freshness_check"
    )
    check_metadata = (
        freshness_checks[0].check_specs_by_output_name["customers_freshness_check"].metadata
    )
    assert check_metadata
    assert check_metadata[FRESHNESS_PARAMS_METADATA_KEY] == JsonMetadataValue(
        {
            TIMEZONE_PARAM_KEY: "UTC",
            LOWER_BOUND_DELTA_PARAM_KEY: 86400,
            DEADLINE_CRON_PARAM_KEY: "0 0 * * *",
        }
    )


def test_dbt_time_partition_freshness_checks(
    test_time_partition_freshness_manifest: Dict[str, Any],
) -> None:
    @dbt_assets(
        manifest=test_time_partition_freshness_manifest,
        partitions_def=DailyPartitionsDefinition(start_date=pendulum.PendulumDateTime(2021, 1, 1)),
    )
    def my_dbt_assets(): ...

    freshness_checks = build_freshness_checks_from_dbt_assets([my_dbt_assets])
    freshness_check = freshness_checks[0]
    # We added a freshness check to the customers table only.
    assert len(freshness_checks) == 1
    assert list(freshness_check.check_keys)[0] == AssetCheckKey(  # noqa
        AssetKey("customers"), "freshness_check"
    )
    check_metadata = (
        freshness_checks[0].check_specs_by_output_name["customers_freshness_check"].metadata
    )
    assert check_metadata
    assert check_metadata[FRESHNESS_PARAMS_METADATA_KEY] == JsonMetadataValue(
        {TIMEZONE_PARAM_KEY: "UTC", DEADLINE_CRON_PARAM_KEY: "0 0 * * *"}
    )
