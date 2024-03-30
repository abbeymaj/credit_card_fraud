# Importing packages
from src.components.model_trainer import ModelTrainer

# Creating a model training pipeline script
if __name__ == '__main__':
    mt = ModelTrainer()
    model_metric = mt.initiate_model_training()
    print(model_metric)