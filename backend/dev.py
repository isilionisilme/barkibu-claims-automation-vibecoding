"""
Development server launcher with hot reload.

This script starts the FastAPI application with uvicorn in development mode.
Hot reload is enabled and configured to exclude non-important paths.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv
    
    # Load environment variables
    load_dotenv()
    
    # Get configuration
    host = os.getenv('BACKEND_HOST', '127.0.0.1')
    port = int(os.getenv('BACKEND_PORT', '8000'))
    
    # Paths to exclude from hot reload watching
    reload_excludes = [
        '*/logs/*',
        '*/tmp/*',
        '*/benchmark/*',
        '*/tests/*',
        '*.pyc',
        '*/__pycache__/*',
        '*/node_modules/*',
        '*/.git/*',
        '*/.vscode/*',
    ]
    
    print(f"Starting development server at http://{host}:{port}")
    print(f"API documentation at http://{host}:{port}/docs")
    print("Hot reload enabled (excluding: logs/, tmp/, benchmark/, tests/)")
    
    # Start uvicorn with hot reload
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=True,
        reload_excludes=reload_excludes,
        log_level="info"
    )
