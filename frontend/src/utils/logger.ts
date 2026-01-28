/**
 * Centralized logging utility for the frontend application.
 * 
 * Log format: [YYYY-MM-DD HH:MM:SS,mmm][FileName][Component][Reason] Message
 * Example: [2026-01-28 13:15:30,123][App.tsx][DocumentUpload][Upload started] Uploading file: invoice_001.pdf
 */

type LogLevel = 'debug' | 'info' | 'warn' | 'error';

interface LogContext {
    component: string;
    reason: string;
    fileName?: string;
}

class Logger {
    private logLevel: LogLevel;
    private enabledLevels: Set<LogLevel>;

    constructor() {
        // Get log level from environment variable
        const envLogLevel = import.meta.env.VITE_LOG_LEVEL as LogLevel || 'info';
        this.logLevel = envLogLevel;

        // Define which levels are enabled based on current log level
        const levelHierarchy: LogLevel[] = ['debug', 'info', 'warn', 'error'];
        const currentLevelIndex = levelHierarchy.indexOf(this.logLevel);
        this.enabledLevels = new Set(levelHierarchy.slice(currentLevelIndex));
    }

    private formatTimestamp(): string {
        const now = new Date();
        const year = now.getFullYear();
        const month = String(now.getMonth() + 1).padStart(2, '0');
        const day = String(now.getDate()).padStart(2, '0');
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        const milliseconds = String(now.getMilliseconds()).padStart(3, '0');

        return `${year}-${month}-${day} ${hours}:${minutes}:${seconds},${milliseconds}`;
    }

    private formatMessage(level: LogLevel, message: string, context: LogContext): string {
        const timestamp = this.formatTimestamp();
        const fileName = context.fileName || 'Unknown';
        const component = context.component;
        const reason = context.reason;

        return `[${timestamp}][${fileName}][${component}][${reason}] ${message}`;
    }

    private shouldLog(level: LogLevel): boolean {
        return this.enabledLevels.has(level);
    }

    debug(message: string, context: LogContext): void {
        if (this.shouldLog('debug')) {
            console.debug(this.formatMessage('debug', message, context));
        }
    }

    info(message: string, context: LogContext): void {
        if (this.shouldLog('info')) {
            console.info(this.formatMessage('info', message, context));
        }
    }

    warn(message: string, context: LogContext): void {
        if (this.shouldLog('warn')) {
            console.warn(this.formatMessage('warn', message, context));
        }
    }

    error(message: string, context: LogContext, error?: Error): void {
        if (this.shouldLog('error')) {
            const formattedMessage = this.formatMessage('error', message, context);
            if (error) {
                console.error(formattedMessage, error);
            } else {
                console.error(formattedMessage);
            }
        }
    }

    setLogLevel(level: LogLevel): void {
        this.logLevel = level;
        const levelHierarchy: LogLevel[] = ['debug', 'info', 'warn', 'error'];
        const currentLevelIndex = levelHierarchy.indexOf(level);
        this.enabledLevels = new Set(levelHierarchy.slice(currentLevelIndex));
    }

    getLogLevel(): LogLevel {
        return this.logLevel;
    }
}

// Export singleton instance
export const logger = new Logger();

// Export types for use in other files
export type { LogLevel, LogContext };
