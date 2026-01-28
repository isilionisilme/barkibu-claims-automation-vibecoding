"""
Centralized logging configuration for the backend application.

Log format: [YYYY-MM-DD HH:MM:SS,mmm][FileName][Component][Reason] Message
Example: [2026-01-28 13:15:30,123][main.py][DocumentProcessor][Upload started] Processing document: invoice_001.pdf
"""

import logging
import os
from pathlib import Path
from datetime import datetime
from typing import Optional


class CustomFormatter(logging.Formatter):
    """Custom formatter that implements the required log format."""
    
    def format(self, record: logging.LogRecord) -> str:
        # Extract filename from pathname
        filename = Path(record.pathname).name
        
        # Get component (logger name or module)
        component = getattr(record, 'component', record.name)
        
        # Get reason (custom field or funcName)
        reason = getattr(record, 'reason', record.funcName)
        
        # Format timestamp
        timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
        
        # Build the log message
        log_message = f"[{timestamp}][{filename}][{component}][{reason}] {record.getMessage()}"
        
        # Add exception info if present
        if record.exc_info:
            log_message += "\n" + self.formatException(record.exc_info)
        
        return log_message


def setup_logging(
    log_level: Optional[str] = None,
    enable_debug: Optional[bool] = None,
    log_dir: Optional[str] = None
) -> logging.Logger:
    """
    Set up centralized logging for the application.
    
    Args:
        log_level: Logging level (debug, info, warn, error). Defaults to env var LOG_LEVEL or 'info'
        enable_debug: Enable debug logging. Defaults to env var ENABLE_DEBUG_LOGS or False
        log_dir: Directory for log files. Defaults to '../logs/backend'
    
    Returns:
        Configured logger instance
    """
    # Get configuration from environment or parameters
    if log_level is None:
        log_level = os.getenv('LOG_LEVEL', 'info')
    
    if enable_debug is None:
        enable_debug = os.getenv('ENABLE_DEBUG_LOGS', 'false').lower() == 'true'
    
    if log_dir is None:
        log_dir = os.getenv('LOG_DIR', '../logs/backend')
    
    # Override log level if debug is enabled
    if enable_debug:
        log_level = 'debug'
    
    # Convert string level to logging constant
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    
    # Create log directory if it doesn't exist
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    
    # Create logger
    logger = logging.getLogger('barkibu')
    logger.setLevel(numeric_level)
    
    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(numeric_level)
    console_handler.setFormatter(CustomFormatter())
    logger.addHandler(console_handler)
    
    # Create file handler for general logs
    general_log_file = log_path / 'general.log'
    file_handler = logging.FileHandler(general_log_file, encoding='utf-8')
    file_handler.setLevel(numeric_level)
    file_handler.setFormatter(CustomFormatter())
    logger.addHandler(file_handler)
    
    # Create file handler for error logs
    error_log_file = log_path / 'error.log'
    error_handler = logging.FileHandler(error_log_file, encoding='utf-8')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(CustomFormatter())
    logger.addHandler(error_handler)
    
    # Prevent propagation to root logger
    logger.propagate = False
    
    return logger


def get_logger(component: str) -> logging.LoggerAdapter:
    """
    Get a logger adapter with component context.
    
    Args:
        component: Component name to include in logs
    
    Returns:
        LoggerAdapter with component context
    """
    logger = logging.getLogger('barkibu')
    return logging.LoggerAdapter(logger, {'component': component})
