from loguru import logger
import sys

def configure_logger():
    logger.remove()
    
    logger.add(sys.stdout, level="INFO", format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>")

    return logger

logger = configure_logger()
