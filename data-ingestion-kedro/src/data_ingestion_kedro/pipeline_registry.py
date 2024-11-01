# src/data_ingestion_kedro/pipeline_registry.py
from typing import Dict
from kedro.pipeline import Pipeline
from data_ingestion_kedro.pipelines.pipeline import create_pipeline

def register_pipelines() -> Dict[str, Pipeline]:
    return {
        "__default__": create_pipeline(),
    }
