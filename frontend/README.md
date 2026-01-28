# Frontend

This directory contains the React + Vite frontend application for the Barkibu Claims Automation system.

## Structure

- `src/` - Source code
  - `main.tsx` - Application entry point
  - `App.tsx` - Root component
  - `utils/logger.ts` - Centralized logging utility
- `package.json` - Node.js dependencies
- `vite.config.ts` - Vite configuration
- `tsconfig.json` - TypeScript configuration
- `index.html` - HTML entry point

## Dependencies

### Core Dependencies

- **react** - UI library
  - Why: Component-based architecture, excellent ecosystem
  - How: Building the user interface
  - Run: See development section below

- **react-dom** - React DOM renderer
  - Why: Required for React web applications
  - How: Rendering React components to the DOM
  - Run: Automatic

- **vite** - Build tool and dev server
  - Why: Fast HMR, modern tooling, excellent DX
  - How: Development server and production builds
  - Run: `npm run dev`

- **typescript** - Type system for JavaScript
  - Why: Type safety, better IDE support, fewer runtime errors
  - How: Type checking and compilation
  - Run: Automatic with Vite

- **vitest** - Testing framework
  - Why: Vite-native, Jest-compatible, fast
  - How: Unit testing
  - Run: `npm run test:unit`

## Development

### Setup

```bash
cd frontend
npm install
```

### Run Development Server

```bash
npm run dev
```

Or use VS Code launch configuration: **[FRONTEND][DEV] Hot reload frontend**

The server will start at `http://localhost:5173` with:
- Hot Module Replacement (HMR) enabled
- Fast refresh for React components
- Logs in browser console with structured format

### Environment Variables

Create a `.env` file in the `frontend/` directory:

```env
VITE_API_URL=http://localhost:8000
VITE_LOG_LEVEL=info
```

## Logging

Centralized logging is implemented in `src/utils/logger.ts`.

**Format**: `[YYYY-MM-DD HH:MM:SS,mmm][FileName][Component][Reason] Message`

**Example**:
```
[2026-01-28 13:15:30,123][App.tsx][DocumentUpload][Upload started] Uploading file: invoice_001.pdf
```

**Log Levels**: debug, info, warn, error

**Control**: Set `VITE_LOG_LEVEL` environment variable

**Location**: Browser console (structured format)

## Testing

### Unit Tests

```bash
npm run test:unit
```

Or use VS Code: **[TEST][UNIT] Frontend unit tests**

Tests are configured with:
- Fail-fast (`bail: 1`)
- Explicit timeouts
- Deterministic termination

## Hot Module Replacement

Vite's HMR automatically watches `src/` directory and updates on changes.

**Excluded from watching**:
- `node_modules/`
- `dist/`
- `logs/`
- `tmp/`

React Fast Refresh is enabled for instant component updates.

## Build

### Development Build

```bash
npm run dev
```

### Production Build

```bash
npm run build
```

Output will be in `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

## Scripts

- `npm run dev` - Start development server with HMR
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally
- `npm run test:unit` - Run unit tests with fail-fast
- `npm run lint` - Run ESLint (if configured)
