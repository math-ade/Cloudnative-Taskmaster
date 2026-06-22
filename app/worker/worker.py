import time
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def process_tasks():
    logger.info("TaskMaster Worker started")
    while True:
        logger.info(f"Worker heartbeat: {datetime.utcnow().isoformat()}")
        time.sleep(30)

if __name__ == '__main__':
    process_tasks()
