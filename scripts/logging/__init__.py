import logging 
import sys

logging.basicConfig(
    handlers =[
        logging.FileHandler('running_logs.log'),
        logging.StreamHandler(sys.stdout)
    ],
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger()


