import json
import random
import time
import uuid
import logging
from datetime import datetime, timezone
from pathlib import Path


SERVICE_NAME = "orders"
ENVIRONMENT = "dev"
LOG_FOLDER = "./.logs"
LOG_FILE = f"{LOG_FOLDER}/orders.log"

Path(LOG_FOLDER).mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.FileHandler(LOG_FILE)]
)

logger = logging.getLogger(SERVICE_NAME)


