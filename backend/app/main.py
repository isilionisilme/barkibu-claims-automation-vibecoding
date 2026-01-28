"""
FastAPI application entry point.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from .logging_config import setup_logging, get_logger

# Load environment variables
load_dotenv()

# Setup logging
setup_logging()
logger = get_logger('main')

# Create FastAPI app
app = FastAPI(
    title="Barkibu Claims Automation",
    description="API for processing veterinary medical records",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Log application startup."""
    logger.info("Application startup", extra={'reason': 'Startup'})


@app.on_event("shutdown")
async def shutdown_event():
    """Log application shutdown."""
    logger.info("Application shutdown", extra={'reason': 'Shutdown'})


@app.get("/")
async def root():
    """Root endpoint."""
    logger.info("Root endpoint accessed", extra={'reason': 'API call'})
    return {
        "message": "Barkibu Claims Automation API",
        "version": "0.1.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
