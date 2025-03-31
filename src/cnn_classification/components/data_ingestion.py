from dataclasses import dataclass
from pathlib import Path
from cnn_classification import *
from cnn_classification.utils.common import read_yaml, create_directory
from cnn_classification.constants import *
import os 
import urllib.request as request
import zipfile
from cnn_classification import logger
from cnn_classification.utils.common import get_size
from cnn_classification.config.configuration import ConfigurationManager
from cnn_classification.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file,) 
            logger.info(f"Downloaded {filename} ")
        else:
            logger.info(f"File already exists")

    def extract_zip_file(self):
        if not os.path.exists(self.config.unzip_dir):
            os.makedirs(self.config.unzip_dir)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
            logger.info(f"Extracted files to {self.config.unzip_dir}")
        else:
            logger.info(f"Directory already exists: {self.config.unzip_dir}")        
        
try:
    config_manager = ConfigurationManager()
    data_ingestion_config = config_manager.get_data_ingestion_config()
    logger.info(f"Data Ingestion Config: {data_ingestion_config}")
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
except Exception as e:
    logger.error(f"Error during data ingestion: {e}")
    raise e