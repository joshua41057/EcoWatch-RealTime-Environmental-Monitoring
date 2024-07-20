// src/components/Alerts.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Alerts = () => {
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        axios.get(`${process.env.REACT_APP_API_URL}/api/alerts`)
            .then(response => setAlerts(response.data))
            .catch(error => console.error('Error fetching alerts:', error));
    }, []);

    return (
        <div>
            <h1>Alerts</h1>
            <ul>
                {alerts.map((alert, index) => (
                    <li key={index}>{alert.message}</li>
                ))}
            </ul>
        </div>
    );
};

export default Alerts;
