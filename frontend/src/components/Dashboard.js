// src/components/Dashboard.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
    const [data, setData] = useState({});

    useEffect(() => {
        axios.get(`${process.env.REACT_APP_API_URL}/api/data`)
            .then(response => setData(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            {/* Render real-time data and charts here */}
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
};

export default Dashboard;
