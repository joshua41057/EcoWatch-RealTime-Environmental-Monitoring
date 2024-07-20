# EcoWatch Frontend

This is the frontend part of the EcoWatch project, which is a comprehensive AI-powered system designed to monitor, analyze, and predict environmental conditions in real-time. This React application provides an interface to visualize data, historical trends, and receive alerts.

## Features

- **Dashboard**: Displays real-time data and predictions.
- **Charts**: Visualizes historical data using charts.
- **Alerts**: Configures and displays alerts based on data thresholds.

## Technologies Used

- **React**: JavaScript library for building user interfaces.
- **Chart.js**: Library for rendering charts.
- **Axios**: HTTP client for making API requests.
- **D3**: Library for data visualization (optional based on usage).

## Setup and Installation

### Prerequisites

- **Node.js**: Ensure you have Node.js installed on your machine.

### Installation

1. **Navigate to the `frontend` directory**:
    ```bash
    cd C:\UCI_CS\EcoWatch-RealTime-Environmental-Monitoring\frontend
    ```

2. **Install dependencies**:
    ```bash
    npm install
    ```

### Running the Project

1. **Start the React development server**:
    ```bash
    npm start
    ```

2. **Open your browser** and navigate to `http://localhost:3000` to view the application.

## Directory Structure

- **`src/components/`**: Contains React components.
    - **`Dashboard.js`**: Component for displaying real-time data.
    - **`Charts.js`**: Component for visualizing historical data.
    - **`Alerts.js`**: Component for displaying alerts.
- **`src/App.js`**: Main application file with routing setup.

## API Integration

- The frontend communicates with the backend API running at `http://localhost:5000`.
- Endpoints:
    - **`/api/data`**: Fetches real-time data.
    - **`/api/predict`**: Provides predictions based on input data.