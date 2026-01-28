# CONTEXT.md

This document captures architectural decisions, stack assumptions, environment variables, ports, and key technical context for this repository.

## Architecture Overview

This is a full-stack application for processing veterinary medical records:

- **Backend**: FastAPI-based REST API for document processing and data extraction
- **Frontend**: React + Vite SPA for document upload and data visualization
- **Processing Pipeline**: Stateful document processing with auditability

## Stack Decisions

### Backend
- **Framework**: FastAPI (Python 3.10+)
- **Why**: Fast, modern, async support, automatic OpenAPI docs, type hints
- **Dev Server**: Uvicorn with hot reload
- **Testing**: pytest with fail-fast configuration
- **Logging**: Custom centralized logging to `./logs`

### Frontend
- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **Why**: Fast HMR, modern tooling, excellent DX
- **Testing**: Vitest (Jest-compatible, Vite-native)
- **Logging**: Custom console logging with structured format

### Default Stack Assumption
Since no specific stack was provided initially, we chose FastAPI + React/Vite as a modern, well-supported default. This stack is modular and can be replaced if needed.

## Environment Variables

### Backend
- `LOG_LEVEL` - Logging level (debug, info, warn, error). Default: `info`
- `BACKEND_PORT` - Port for backend server. Default: `8000`
- `BACKEND_HOST` - Host for backend server. Default: `127.0.0.1`
- `ENABLE_DEBUG_LOGS` - Enable debug logging (true/false). Default: `false`

### Frontend
- `VITE_API_URL` - Backend API URL. Default: `http://localhost:8000`
- `VITE_LOG_LEVEL` - Frontend logging level. Default: `info`

## Ports

- **Backend**: 8000 (configurable via `BACKEND_PORT`)
- **Frontend**: 5173 (Vite default, configurable in vite.config.ts)

## Logging Strategy

### Backend Logging
- **Location**: `./logs/` directory
- **Format**: `[YYYY-MM-DD HH:MM:SS,mmm][FileName][Component][Reason] Message`
- **Categories**: Split by feature/module
- **Control**: Use `LOG_LEVEL` and `ENABLE_DEBUG_LOGS` environment variables
- **Implementation**: Custom logging configuration in `backend/app/logging_config.py`

### Frontend Logging
- **Format**: Same as backend for consistency
- **Control**: Runtime toggle via `VITE_LOG_LEVEL`, build-time via env vars
- **Implementation**: Custom logger utility in `frontend/src/utils/logger.ts`

## Hot Reload Configuration

### Backend
- **Tool**: Uvicorn with `--reload` flag
- **Exclusions**: `logs/`, `tmp/`, `benchmark/`, `tests/`, `*.pyc`, `__pycache__/`
- **Watch**: `backend/app/` directory

### Frontend
- **Tool**: Vite HMR (built-in)
- **Exclusions**: `node_modules/`, `dist/`, `logs/`, `tmp/`
- **Fast Refresh**: Enabled for React components

## Testing Strategy

### Unit Tests
- **Backend**: pytest with `--maxfail=1` (fail-fast)
- **Frontend**: Vitest with `bail: 1` (fail-fast)
- **Timeouts**: All tests have explicit timeouts
- **Location**: `tests/unit/`

### Regression Tests
- **Purpose**: Simulate real client behavior (frontend → backend)
- **Framework**: pytest for end-to-end flows
- **Configuration**: Fail-fast, deterministic termination
- **Location**: `tests/regression/`

### Fail-Fast Configuration
- pytest: `--maxfail=1 --exitfirst`
- Vitest: `bail: 1` in config
- All tests exit immediately on uncaught exceptions, runtime errors, or failed assertions

## Benchmarking

- **Location**: `benchmark/`
- **Framework**: Custom Python scripts using `timeit` or `pytest-benchmark`
- **Metrics**: Latency, throughput, memory usage
- **Output**: Structured JSON or console output with measurable metrics

## CI/CD

- **Platform**: GitHub Actions
- **Triggers**: Pull requests, pushes to main
- **Steps**: Unit tests → Regression tests
- **Fail-Fast**: CI fails immediately on first error
- **Configuration**: `.github/workflows/ci.yml`

## Dependency Management

### Backend
- **File**: `backend/requirements.txt`
- **Documentation**: Each major dependency documented in backend/README.md

### Frontend
- **File**: `frontend/package.json`
- **Documentation**: Each major dependency documented in frontend/README.md

### Rule
No dependency is added without documenting:
1. Why it is needed
2. How it is used
3. How to run it (if applicable)

## Folder Structure Decisions

- **tmp/**: One-off, throwaway scripts only. Not for reusable code.
- **tests/**: General tests with subdirectories for unit and regression
- **benchmark/**: Performance tests (chosen over `tests/benchmarks/` for clarity)
- **logs/**: Application logs, excluded from version control
- **Every folder**: Contains README.md explaining purpose and usage

## Guardrails

1. **Minimal viable structure** over over-engineering
2. **Consistency beats cleverness**
3. **Fail fast** rather than partially comply
4. **Document everything** - no undocumented dependencies or decisions
