// src/components/Weather.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Weather = () => {
    const [weather, setWeather] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:5000/api/weather')
            .then(response => {
                setWeather(response.data);
            })
            .catch(err => {
                setError('Error fetching weather data');
                console.error('Error fetching weather data:', err);
            });
    }, []);

    if (error) {
        return <div>{error}</div>;
    }

    if (!weather) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Weather Data</h1>
            <p>Temperature: {weather.temperature} °F</p>
            <p>Humidity: {weather.humidity} %</p>
            <p>Condition: {weather.condition}</p>
        </div>
    );
};

export default Weather;
