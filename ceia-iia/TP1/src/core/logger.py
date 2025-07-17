from loguru import logger as _logger
import sys

def configure_logger(log_level="INFO"):
    _logger.remove()
    
    _logger.add(sys.stdout, level=log_level, format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>")

    return _logger

logger = configure_logger()
