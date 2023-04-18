import os, sys
from signLanguage.exception import SignException
from signLanguage.logger import logging
from signLanguage.components.data_ingestion import DataIngestion

from signLanguage.entity.config_entity import (DataIngestionConfig)
from signLanguage.entity.artifact_entity import (DataIngestionArtifact)


class TrainPipeline:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info(f"Entered the start_data_ingestion method of TrainPipeline class")
            logging.info(f"Getting the data from url")
            
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
                )
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Got the data from url")
            logging.info(
                         "Exited the start_data_ingestion method of TrainPipeline class"
                         )
            
            return data_ingestion_artifact
        except SignException as e:
            raise SignException(e, sys)
        
    
    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise SignException(e, sys)
        

