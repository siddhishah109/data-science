import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

function generateForecast(data, windowSize) {
    const forecastedData = [...data];

    for (let i = 0; i < data.length; i++) {
        if (i >= windowSize) {
            const sum = data.slice(i - windowSize, i).reduce((acc, val) => acc + val.value, 0);
            const average = sum / windowSize;
            forecastedData.push({ name: `Forecast ${i}`, value: average });
        }
    }

    return forecastedData;
}

function TrendGraph({ data, windowSize = 3 }) {
    const forecastedData = generateForecast(data, windowSize);

    return (
        <LineChart width={500} height={300} data={forecastedData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="value" stroke="#8884d8" />
        </LineChart>
    );
}

export default TrendGraph;
