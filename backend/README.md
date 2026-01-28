# Backend

This directory contains the FastAPI backend application for processing veterinary medical records.

## Structure

- `app/` - Main application code
  - `main.py` - FastAPI application entry point
  - `logging_config.py` - Centralized logging configuration
- `requirements.txt` - Python dependencies
- `dev.py` - Development server launcher with hot reload

## Dependencies

### Core Dependencies

- **fastapi** - Modern web framework for building APIs
  - Why: Fast, async support, automatic OpenAPI docs, type hints
  - How: Main application framework
  - Run: See development section below

- **uvicorn[standard]** - ASGI server
  - Why: Production-ready server with hot reload support
  - How: Runs the FastAPI application
  - Run: `uvicorn app.main:app --reload`

- **python-dotenv** - Environment variable management
  - Why: Load configuration from .env files
  - How: Automatically loads .env on startup
  - Run: Automatic

- **pytest** - Testing framework
  - Why: Industry standard, excellent plugin ecosystem
  - How: Unit and regression testing
  - Run: `pytest tests/ --maxfail=1 --exitfirst -v`

## Development

### Setup

```bash
cd backend
pip install -r requirements.txt
```

### Run Development Server

```bash
python dev.py
```

Or use VS Code launch configuration: **[BACKEND][DEV] Hot reload backend**

The server will start at `http://localhost:8000` with:
- Hot reload enabled
- API documentation at `/docs`
- Logs written to `../logs/backend/`

### Environment Variables

Create a `.env` file in the `backend/` directory:

```env
LOG_LEVEL=info
BACKEND_PORT=8000
BACKEND_HOST=127.0.0.1
ENABLE_DEBUG_LOGS=false
```

## Logging

Centralized logging is configured in `app/logging_config.py`.

**Format**: `[YYYY-MM-DD HH:MM:SS,mmm][FileName][Component][Reason] Message`

**Example**:
```
[2026-01-28 13:15:30,123][main.py][DocumentProcessor][Upload started] Processing document: invoice_001.pdf
```

**Log Levels**: debug, info, warn, error

**Control**: Set `LOG_LEVEL` or `ENABLE_DEBUG_LOGS` environment variables

**Location**: `../logs/backend/` (split by category/feature)

## Testing

### Unit Tests

```bash
pytest tests/unit/ --maxfail=1 --exitfirst -v
```

Or use VS Code: **[TEST][UNIT] Backend unit tests**

### Regression Tests

```bash
pytest tests/regression/ --maxfail=1 --exitfirst -v
```

Or use VS Code: **[TEST][REGRESSION] Full regression suite**

All tests are configured with:
- Fail-fast on first error
- Explicit timeouts
- Deterministic termination

## Hot Reload

The development server watches `app/` directory and reloads on changes.

**Excluded from watching**:
- `logs/`
- `tmp/`
- `benchmark/`
- `tests/`
- `*.pyc`
- `__pycache__/`

## API Documentation

When the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
