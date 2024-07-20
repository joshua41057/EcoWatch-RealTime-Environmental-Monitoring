// src/components/Charts.js
import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

const Charts = () => {
    const [chartData, setChartData] = useState({});

    useEffect(() => {
        axios.get(`${process.env.REACT_APP_API_URL}/api/data`)
            .then(response => {
                const data = response.data; // Assuming data is in a format suitable for charts
                setChartData({
                    labels: data.labels,
                    datasets: [
                        {
                            label: 'Historical Data',
                            data: data.values,
                            borderColor: 'rgba(75, 192, 192, 1)',
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        },
                    ],
                });
            })
            .catch(error => console.error('Error fetching chart data:', error));
    }, []);

    return (
        <div>
            <h1>Charts</h1>
            <Line data={chartData} />
        </div>
    );
};

export default Charts;
