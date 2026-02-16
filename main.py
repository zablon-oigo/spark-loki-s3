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

regions = ["kenya", "uganda", "tanzania"]
payment_methods = ["mpesa", "card", "bank_transfer"]
devices = ["mobile", "web"]

def generate_event():
    success = random.random() > 0.1
    trace_id = str(uuid.uuid4())

    if not success:
        response_time = random.randint(400, 1200)
    else:
        response_time = random.randint(50, 300)

    event = {
        "service": SERVICE_NAME,
        "environment": ENVIRONMENT,
        "trace_id": trace_id,
        "event": "order_created",
        "order_id": str(uuid.uuid4()),
        "user_id": random.randint(1, 10000),
        "region": random.choice(regions),
        "payment_method": random.choice(payment_methods),
        "device": random.choice(devices),
        "currency": "KES",
        "amount": round(random.uniform(100, 1000), 2),
        "status": "success" if success else "failed",
        "retry_count": random.randint(0, 3),
        "response_time_ms": response_time,
        "event_time": datetime.now(timezone.utc).isoformat()
    }

    return event, success


