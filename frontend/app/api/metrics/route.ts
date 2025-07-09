// app/api/metrics/route.ts
import { NextResponse } from 'next/server';
import { Pool } from 'pg';

// PostgreSQL connection pool configuration
const pool = new Pool({
    user: 'postgres',       
    host: 'localhost',
    database: 'BMS',         
    password: '1234',        
    port: 5432,
    });

    export async function GET() {
    try {
        // Query to get the latest 10 BMS readings
        const result = await pool.query(
        'SELECT * FROM bms_metrics ORDER BY timestamp DESC LIMIT 10'
        );

        // Return the result rows as JSON
        return NextResponse.json(result.rows);
    } catch (error: any) {
        // Log the actual error to the terminal for debugging
        console.error('DB Error:', error.message);

        // Return a 500 error to the client with error message
        return NextResponse.json(
        { error: error.message || 'Database query failed' },
        { status: 500 }
        );
    }
}
