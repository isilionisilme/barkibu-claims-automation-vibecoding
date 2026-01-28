# Barkibu Claims Automation

This system allows vets to upload docs with a pet's medical record, extracts and analyzes its content and identifies and structure the most relevant info in a standardized way.

## Features

### Backend Features
- Document upload and processing
- Medical record data extraction
- Stateful processing pipeline with auditability
- RESTful API with automatic OpenAPI documentation
- Centralized logging with configurable levels
- Hot reload development server

### Frontend Features
- Document upload interface
- Data visualization and review
- Real-time processing status
- Hot module replacement (HMR) for fast development

## Configuration Parameters

### Backend Configuration

Environment variables (create `.env` file in `backend/` directory):

- `LOG_LEVEL` - Logging level: `debug`, `info`, `warn`, `error` (default: `info`)
- `BACKEND_PORT` - Server port (default: `8000`)
- `BACKEND_HOST` - Server host (default: `127.0.0.1`)
- `ENABLE_DEBUG_LOGS` - Enable debug logging: `true` or `false` (default: `false`)

### Frontend Configuration

Environment variables (create `.env` file in `frontend/` directory):

- `VITE_API_URL` - Backend API URL (default: `http://localhost:8000`)
- `VITE_LOG_LEVEL` - Frontend logging level (default: `info`)

## How to Run

### Prerequisites

- Python 3.10 or higher
- Node.js 18 or higher
- npm or yarn

### Quick Start with VS Code

The easiest way to run this project is using VS Code's Run and Debug panel (Ctrl+Shift+D):

1. **[BACKEND][DEV] Hot reload backend** - Start backend with hot reload
2. **[FRONTEND][DEV] Hot reload frontend** - Start frontend with HMR
3. **[TEST][UNIT] Backend unit tests** - Run unit tests
4. **[TEST][REGRESSION] Full regression suite** - Run regression tests
5. **[BENCH][API] API benchmarks** - Run performance benchmarks

### Manual Setup

#### Backend Development

```bash
cd backend
pip install -r requirements.txt
python dev.py
```

Backend will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

#### Frontend Development

```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at `http://localhost:5173`

### Running Tests

#### Unit Tests

```bash
# Backend unit tests
cd backend
pytest tests/unit/ --maxfail=1 --exitfirst -v

# Frontend unit tests
cd frontend
npm run test:unit
```

#### Regression Tests

```bash
# Full regression suite (requires backend running)
pytest tests/regression/ --maxfail=1 --exitfirst -v
```

#### All Tests

```bash
# Run all tests (unit + regression)
pytest tests/ --maxfail=1 --exitfirst -v
```

### Running Benchmarks

```bash
# API benchmarks
python benchmark/bench_api.py

# Or use VS Code launch configuration:
# [BENCH][API] API benchmarks
```

## Project Structure

- `backend/` - FastAPI backend application
- `frontend/` - React + Vite frontend application
- `tests/` - Unit and regression tests
  - `tests/unit/` - Unit tests
  - `tests/regression/` - End-to-end regression tests
- `benchmark/` - Performance benchmarks
- `logs/` - Application logs (not committed to git)
- `tmp/` - Temporary scripts and one-off files

Each folder contains its own README.md with detailed documentation.

## Logging

Logs are written to the `logs/` directory with the following format:

```
[YYYY-MM-DD HH:MM:SS,mmm][FileName][Component][Reason] Message
```

Example:
```
[2026-01-28 13:15:30,123][main.py][DocumentProcessor][Upload started] Processing document: invoice_001.pdf
```

### Controlling Log Levels

**Backend**: Set `LOG_LEVEL` environment variable or `ENABLE_DEBUG_LOGS=true`

**Frontend**: Set `VITE_LOG_LEVEL` environment variable

## CI/CD

GitHub Actions automatically runs tests on pull requests:

- Unit tests (backend + frontend)
- Regression tests
- Fails fast on first error

See `.github/workflows/ci.yml` for details.

## Documentation

- **[AGENTS.md](file:///d:/Git/barkibu-claims-automation-vibecoding/AGENTS.md)** - Entry point for AI agents
- **[CONTEXT.md](file:///d:/Git/barkibu-claims-automation-vibecoding/CONTEXT.md)** - Architecture and technical decisions
- **Folder READMEs** - Each major folder has detailed documentation

## Development Guidelines

1. **Fail Fast** - All tests and processes exit immediately on errors
2. **Hot Reload** - Use dev servers for fast iteration
3. **Centralized Logging** - Use the logging infrastructure, not print statements
4. **Document Dependencies** - Every new dependency must be documented
5. **Test Everything** - Unit tests + regression tests for all features

## Support

For questions about architecture or technical decisions, see [CONTEXT.md](file:///d:/Git/barkibu-claims-automation-vibecoding/CONTEXT.md).
