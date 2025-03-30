from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage1_dataingestion import DataIngestionTrainingPipeLine
from src.textSummarizer.pipeline.stage2_datatransformation import DataTransformationTrainingPipeLine

stage_name="Data Ingestion"
try:
    logger.info(f"{'>>'*20} {stage_name} started {'<<'*20}")
    data_ingestion=DataIngestionTrainingPipeLine()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"{'>>'*20} {stage_name} completed {'<<'*20}")

except Exception as e:
    logger.exception(e)
    raise e

stage_name="Data Transformation"
try:
    logger.info(f"{'>>'*20} {stage_name} started {'<<'*20}")
    data_transformation=DataTransformationTrainingPipeLine()
    data_transformation.initiate_data_transformation()
    logger.info(f"{'>>'*20} {stage_name} completed {'<<'*20}")

except Exception as e:
    logger.exception(e)
    raise e