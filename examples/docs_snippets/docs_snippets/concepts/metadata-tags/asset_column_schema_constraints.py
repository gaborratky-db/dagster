from dagster import (
    AssetKey,
    MaterializeResult,
    TableColumn,
    TableColumnConstraints,
    TableSchema,
    asset,
)


@asset(
    deps=[AssetKey("source_bar"), AssetKey("source_baz")],
    metadata={
        "dagster/column_schema": TableSchema(
            columns=[
                TableColumn(
                    "name",
                    "string",
                    description="The name of the person",
                ),
                TableColumn(
                    "age",
                    "int",
                    description="The age of the person",
                    constraints=TableColumnConstraints(nullable=False, other=[">0"]),
                ),
            ]
        )
    },
)
def my_asset(): ...
