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

function TrendGraph({ data, windowSize = 3, xAxisProps = {}, yAxisProps = {}, cartesianGridProps = {}, tooltipProps = {}, legendProps = {}, lineProps = {}, ...rest }) {
    const forecastedData = generateForecast(data, windowSize);

    return (
        <LineChart width={500} height={300} data={forecastedData} {...rest}>
            <CartesianGrid {...cartesianGridProps} />
            <XAxis {...xAxisProps} />
            <YAxis {...yAxisProps} />
            <Tooltip {...tooltipProps} />
            <Legend {...legendProps} />
            <Line type="monotone" dataKey="value" {...lineProps} />
        </LineChart>
    );
}

export default TrendGraph;



{/* 


The purpose of the provided React component, TrendGraph, is to generate a line chart with the capability to forecast future data points based on a moving average window. It's built using the Recharts library, a popular charting library for React applications.


 example use: 

<TrendGraph
    data={data}
    width={600}
    height={400}
    margin={{ top: 20, right: 30, bottom: 20, left: 30 }}
    lineColor="#ff0000"
    strokeWidth={2}
    xAxisProps={{
        dataKey: 'name',
        label: { value: 'Month', position: 'insideBottomRight', offset: -10 }
    }}
    yAxisProps={{ label: { value: 'Value', angle: -90, position: 'insideLeft' } }}
    cartesianGridProps={{ strokeDasharray: '3 3', vertical: false }}
    tooltipProps={{ cursor: { stroke: 'red', strokeWidth: 2 } }}
    legendProps={{ align: 'center', verticalAlign: 'top', height: 36 }}
    lineProps={{ stroke: '#ff0000', strokeWidth: 2, dot: false }}
/> 


*/}
