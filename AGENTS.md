# AGENTS.md

This document serves as the entry point for AI agents working on this repository.

## Quick Links

- **[CONTEXT.md](file:///d:/Git/barkibu-claims-automation-vibecoding/CONTEXT.md)** - Architecture, stack decisions, environment variables, and technical context
- **[README.md](file:///d:/Git/barkibu-claims-automation-vibecoding/README.md)** - User-facing documentation, features, and how to run the project

## Agent Guidelines

1. **Read CONTEXT.md first** to understand architectural decisions and stack assumptions
2. **Consult README.md** for feature documentation and operational instructions
3. **Follow the strict rules** defined in the bootstrapping configuration
4. **Maintain documentation** - every change should be reflected in relevant docs
5. **Fail fast** - if a MUST rule cannot be satisfied, stop and explain the blocker

## Repository Structure

All major folders contain their own README.md explaining purpose and usage:

- `backend/` - Backend application code
- `frontend/` - Frontend application code
- `tests/` - Unit and regression tests
- `benchmark/` - Performance benchmarks
- `tmp/` - Temporary/throwaway scripts only
- `logs/` - Application logs (not committed)

## Running the Project

All runnable workflows are defined in `.vscode/launch.json`. Use VS Code's Run and Debug panel to:

- Start backend/frontend in dev mode with hot reload
- Run unit tests, regression tests, or benchmarks
- All configurations follow the naming convention: `[CATEGORY][SUBCATEGORY] Description`
