// app/api/metrics/route.ts
import { NextResponse } from 'next/server'; // its used to send HTTP response in Next.js API routes
import { Pool } from 'pg';

// PostgreSQL connection pool configuration
const pool = new Pool({
    user: 'postgres',       
    host: 'localhost',
    database: 'BMS',         
    password: '1234',        
    port: 5432,
    });

    //this defines an API handler
    export async function GET() {
    try {
        // Query to get the latest 10 BMS readings
        const result = await pool.query(
        'SELECT * FROM bms_metrics ORDER BY timestamp DESC LIMIT 10'
        );

        // Return the result rows as JSON
        return NextResponse.json(result.rows);
    } catch(error: unknown){
        if(error instanceof Error){
            console.error('DB Error', error.message);
            return NextResponse.json(
                {error: error.message},
                {status: 500}
            );
        } else{
            return NextResponse.json(
                {error: 'Unknown error occured'},
                {status: 500}
            );
        }
    }
}


//SUMMARY
// connect to a psql
// define a GET API route at api/metrics path
//Fetches the latest 10 BMS records
// return then as a json response
//