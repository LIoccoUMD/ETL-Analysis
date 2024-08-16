import kaggle
import logging

logging.basicConfig(filename='log/extract.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting Kaggle dataset extraction.")

try:
    
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files("niharika41298/gym-exercise-data", path="data\extracted", unzip=True)
    logging.info("Dataset downloaded and extracted successfully.")
    kaggle.api.dataset_metadata("niharika41298/gym-exercise-data", path="data\extracted")
    logging.info("Dataset metadata downloaded successfully.")
    
except Exception as e:
    logging.error(f"Error during dataset extraction: {e}")
    raise