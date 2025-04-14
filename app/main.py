from scripts.preprocess import preprocessing_dataset
import app.app
import subprocess
from scripts.logging import logger


def run_app():
    subprocess.Popen(["streamlit", "run", "app.py"])


# Data Preprocessing Stage
STAGE_NAME = "DataPreprocessing"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    preprocessing_dataset()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# Model Training Stage
STAGE_NAME = "ModelTraining"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    from scripts.train import train_model
    train_model()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# Model Evaluation Stage 
STAGE_NAME = "ModelEvaluation"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    from scripts.evaluate import evaluate_model
    evaluate_model() 
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# Running the UI 
try:
    logger.info("Running UI")
    run_app() 
    logger.info("UI is ready")
except Exception as e:
    logger.exception(e)
    raise e