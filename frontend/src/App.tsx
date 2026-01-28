import { useState, useEffect } from 'react'
import { logger } from './utils/logger'

function App() {
    const [message, setMessage] = useState<string>('Loading...')

    useEffect(() => {
        logger.info('App component mounted', {
            component: 'App',
            reason: 'Component lifecycle',
            fileName: 'App.tsx'
        });

        // Fetch from backend
        const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';

        fetch(`${apiUrl}/`)
            .then(res => res.json())
            .then(data => {
                logger.info('Backend connection successful', {
                    component: 'App',
                    reason: 'API call',
                    fileName: 'App.tsx'
                });
                setMessage(data.message || 'Connected to backend');
            })
            .catch(error => {
                logger.error('Failed to connect to backend', {
                    component: 'App',
                    reason: 'API call',
                    fileName: 'App.tsx'
                }, error);
                setMessage('Failed to connect to backend. Make sure the backend is running.');
            });
    }, []);

    return (
        <div style={{
            padding: '2rem',
            fontFamily: 'system-ui, -apple-system, sans-serif',
            maxWidth: '800px',
            margin: '0 auto'
        }}>
            <h1>Barkibu Claims Automation</h1>
            <p>{message}</p>
            <div style={{
                marginTop: '2rem',
                padding: '1rem',
                backgroundColor: '#f5f5f5',
                borderRadius: '8px'
            }}>
                <h2>System Status</h2>
                <p>Frontend: ✅ Running</p>
                <p>Backend: {message.includes('Failed') ? '❌ Not connected' : '✅ Connected'}</p>
            </div>
            <div style={{ marginTop: '2rem', fontSize: '0.9rem', color: '#666' }}>
                <p>Check the browser console to see structured logs.</p>
                <p>Log format: [YYYY-MM-DD HH:MM:SS,mmm][FileName][Component][Reason] Message</p>
            </div>
        </div>
    )
}

export default App
