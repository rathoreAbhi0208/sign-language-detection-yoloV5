import os, sys
from signLanguage.exception import SignException
from signLanguage.logger import logging
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation
from signLanguage.components.model_trainer import ModelTrainer

from signLanguage.entity.config_entity import (DataIngestionConfig,
                                               DataValidationConfig,
                                               ModelTrainerConfig)

from signLanguage.entity.artifact_entity import (DataIngestionArtifact,
                                                 DataValidationArtifact,
                                                 ModelTrainerArtifact)





class TrainPipeline:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()


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
        
    def start_data_validation(
            self,data_ingestion_artifact:DataIngestionArtifact
    )->DataValidationArtifact:
        
        logging.info(f"Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info(f"Performed the data validation")
            logging.info(
                "Exited the data validation method of TrainPipeline class"
            )

            return data_validation_artifact
        
        except SignException as e:
            raise SignException(e, sys)
        
    def start_model_trainer(self
    ) -> ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer(
                model_trainer_config=self.model_trainer_config,
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)
        
    
    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
            )


            if data_validation_artifact.validation_status == True:
                model_trainer_artifact = self.start_model_trainer()
                #model_pusher_artifact = self.start_model_pusher(model_trainer_artifact=model_trainer_artifact,s3=self.s3_operations)

            
            else:
                raise Exception("Your data is not in correct format")


        except Exception as e:
            raise SignException(e, sys)
        
    
    
        

