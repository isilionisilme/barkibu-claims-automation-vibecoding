import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    server: {
        port: 5173,
        host: true,
        watch: {
            // Exclude non-important paths from watching
            ignored: [
                '**/node_modules/**',
                '**/dist/**',
                '**/logs/**',
                '**/tmp/**',
                '**/.git/**',
            ]
        }
    },
    build: {
        outDir: 'dist',
        sourcemap: true,
    },
})
