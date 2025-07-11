// app/page.tsx
'use client'; // must be first line if using hooks

import { useEffect, useState } from 'react';

type BmsMetric = {
  id: number;
  bms_id: string;
  temperature: number;
  voltage: number;
  current: number;
  soc: number;
  soh: number;
  fan_status: string;
  timestamp: string;
};

export default function Page() {
  const [data, setData] = useState<BmsMetric[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('/api/metrics')
      .then(async (res) => {
        const json = await res.json();
        if (Array.isArray(json)) {
          setData(json);
        } else {
          setError(json.error || 'Unexpected API response');
        }
      })
      .catch((err) => setError(err.message));
  }, []);

  return (
    <main style={{ padding: '20px' }}>
      <h1>BMS Metrics Dashboard</h1>
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}

      <table border={1} cellPadding={10} style={{ marginTop: '20px', width: '100%' }}>
        <thead>
          <tr>
            <th>BMS ID</th><th>Temp</th><th>Voltage</th><th>Current</th>
            <th>SOC</th><th>SOH</th><th>Fan</th><th>Time</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row) => (
            <tr key={row.id}>
              <td>{row.bms_id}</td>
              <td>{row.temperature}</td>
              <td>{row.voltage}</td>
              <td>{row.current}</td>
              <td>{row.soc}</td>
              <td>{row.soh}</td>
              <td>{row.fan_status}</td>
              <td>{row.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}