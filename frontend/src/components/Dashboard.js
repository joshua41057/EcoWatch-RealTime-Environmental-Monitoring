import React, { useState, useEffect } from 'react';

const Dashboard = () => {
    const [weatherData, setWeatherData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch('http://localhost:5000/api/data')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setWeatherData(data);
                setLoading(false);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                setError(error);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    if (!weatherData || weatherData.length === 0) {
        return <div>No data available</div>;
    }

    // Assuming the API returns an array of weather objects, take the first one for this example
    const weather = weatherData[0];

    return (
        <div>
            <h1>Current Weather in {weather.name}</h1>
            <p>Temperature: {weather.main.temp}°C</p>
            <p>Feels Like: {weather.main.feels_like}°C</p>
            <p>Minimum Temperature: {weather.main.temp_min}°C</p>
            <p>Maximum Temperature: {weather.main.temp_max}°C</p>
            <p>Humidity: {weather.main.humidity}%</p>
            <p>Pressure: {weather.main.pressure} hPa</p>
            <p>Weather Description: {weather.weather[0].description}</p>
            <p>Wind Speed: {weather.wind.speed} m/s</p>
        </div>
    );
};

export default Dashboard;
