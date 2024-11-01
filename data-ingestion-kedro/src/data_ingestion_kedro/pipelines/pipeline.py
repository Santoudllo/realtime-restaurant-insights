# src/data_ingestion_kedro/pipelines/pipeline.py
from kedro.pipeline import Pipeline, node
from data_ingestion_kedro.nodes.data_collection import fetch_data_from_api
from data_ingestion_kedro.nodes.data_insertion import insert_data_to_mongodb

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=fetch_data_from_api,
                inputs=dict(api_url="params:api_url", limit="params:limit"),
                outputs=["raw_data", "total_records"],
                name="fetch_data_node",
            ),
            node(
                func=insert_data_to_mongodb,
                inputs="raw_data",
                outputs="inserted_count",
                name="insert_data_node",
            ),
        ]
    )
