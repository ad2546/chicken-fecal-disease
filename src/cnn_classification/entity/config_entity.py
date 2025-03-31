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


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
