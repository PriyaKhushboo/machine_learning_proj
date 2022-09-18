
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, \
ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig


class Configuration:
    def __init__(self):
        pass

    def get_data_ingetion_config(self) -> DataIngestionConfig:
        pass

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self):
        pass

    def get_model_trainer_config(self):
        pass
    
    def get_model_evaluation_config(self):
        pass

    def get_model_pusher_config(self):
        pass

    def get_training_pipeline_config(self):
        pass