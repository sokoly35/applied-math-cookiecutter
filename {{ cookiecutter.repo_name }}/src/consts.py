import os
from pathlib import Path

PROJECT_ROOT_DIR = Path(__file__).parent.parent

MODELS = "models"
DATA = "data"
RAW = "raw"
PROCESSED = "processed"
INTERIM = "interim"
MEDIA = "media"

DATA_PATH = os.path.join(PROJECT_ROOT_DIR, DATA)

RAW_DATA_PATH = os.path.join(PROJECT_ROOT_DIR, DATA, RAW)
PROCESSED_DATA_PATH = os.path.join(PROJECT_ROOT_DIR, DATA, PROCESSED)
INTERIM_DATA_PATH = os.path.join(PROJECT_ROOT_DIR, DATA, INTERIM)

MODELS_PATH = os.path.join(PROJECT_ROOT_DIR, MODELS)
MEDIA_PATH = os.path.join(PROJECT_ROOT_DIR, MEDIA)
