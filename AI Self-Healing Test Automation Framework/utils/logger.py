"""
Logging module for WhatsApp AI Automation Framework
Provides centralized logging configuration and utilities
"""

import logging
import sys
from pathlib import Path
from utils.config import LOG_LEVEL, LOG_FORMAT, LOG_FILE

# Create logs directory if it doesn't exist
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


class ColoredFormatter(logging.Formatter):
    """Custom formatter with color support for console output"""

    COLORS = {
        "DEBUG": "\033[36m",      # Cyan
        "INFO": "\033[32m",       # Green
        "WARNING": "\033[33m",    # Yellow
        "ERROR": "\033[31m",      # Red
        "CRITICAL": "\033[35m",   # Magenta
    }
    RESET = "\033[0m"

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.RESET)
        record.levelname = f"{log_color}{record.levelname}{self.RESET}"
        return super().format(record)


def get_logger(name):
    """
    Get or create a logger with the specified name
    
    Args:
        name (str): Logger name, typically __name__
    
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # Avoid duplicate handlers
    if logger.handlers:
        return logger
    
    # Set log level
    logger.setLevel(LOG_LEVEL)
    
    # Create formatters
    formatter = logging.Formatter(LOG_FORMAT)
    colored_formatter = ColoredFormatter(LOG_FORMAT)
    
    # File handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(colored_formatter)
    logger.addHandler(console_handler)
    
    return logger


# Module-level logger
logger = get_logger(__name__)


def log_step(step_name):
    """Decorator to log test steps"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.info(f"Starting: {step_name}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"Completed: {step_name}")
                return result
            except Exception as e:
                logger.error(f"Failed: {step_name} - {str(e)}")
                raise
        return wrapper
    return decorator
