# Backend Documentation for EcoWatch

This directory contains the backend components for the EcoWatch project, including scripts for data collection, model training, and serving predictions via a Flask API. This README provides detailed instructions for setting up and using each component.

## Backend Components

### `model.py`

**Description**: This script is responsible for creating, training, and predicting with a deep learning model.

**Functions**:
- `create_model()`: Defines and compiles an LSTM model.
- `train_model()`: Loads air quality data, preprocesses it, trains the LSTM model, and saves it.
- `predict(data)`: Loads the trained model and makes predictions on new data.

**Usage**:

- **Train the Model**:
    ```sh
    python model.py
    ```
  This will train the model using data from `../data/air_quality.csv` and save the trained model as `environmental_model.keras`.

- **Make Predictions**:
    ```python
    from model import predict

    data = [0.5, 0.6, 0.7]
    prediction = predict(data)
    print(prediction)
    ```
  Replace `data` with your input for predictions. Ensure the `environmental_model.keras` file exists before running predictions.

### `data_collection.py`

**Description**: This script collects air quality and weather data from external APIs and saves them locally.

**Functions**:
- `fetch_air_quality(lat, lon, ...)`: Fetches air quality data from the OpenAQ API and saves it to `../data/air_quality.csv`.
- `get_weather_data(lat, lon, units)`: Fetches weather data from the OpenWeatherMap API.
- `collect_weather_data(num_collections, interval)`: Collects weather data at regular intervals and saves it to `weather_data.json`.
- `stop_data_collection()`: Allows stopping the data collection process via user input.
- `signal_handler(sig, frame)`: Handles interrupt signals (e.g., Ctrl+C) to gracefully stop data collection.

**Usage**:

- **Fetch Air Quality Data**:
    ```sh
    python data_collection.py
    ```
  This will fetch air quality data and save it to `../data/air_quality.csv`.

- **Collect Weather Data**:
    ```sh
    python data_collection.py
    ```
  This will start collecting weather data, saving it to `weather_data.json`. Press 'q' or send an interrupt signal to stop the data collection.

**Configuration**:
- **API Keys**: Ensure the `WEATHER_API_KEY` variable is set with a valid API key from OpenWeatherMap.
- **Paths**: Adjust the file paths if necessary, especially if running scripts from different directories.

### `app.py`

**Description**: This script sets up a Flask API for serving predictions from the trained model.

**Functions**:
- `load_model()`: Loads the trained TensorFlow model from the specified path.
- `get_data()`: Placeholder for data fetching logic (currently returns a success message).
- `predict()`: Receives input data via POST request, processes it, and returns predictions.

**Usage**:

- **Run the Flask API**:
    ```sh
    python app.py
    ```
  This will start the Flask server on `http://127.0.0.1:5000`.

- **Interact with the API**:
    - **Fetch Data (Placeholder)**:
      ```sh
      curl -X GET http://127.0.0.1:5000/api/data
      ```
    - **Get Predictions**:
      ```sh
      curl -X POST http://127.0.0.1:5000/api/predict -H "Content-Type: application/json" -d "{\"data\": [0.5, 0.6, 0.7]}"
      ```
      Ensure the `environmental_model.keras` file is in the `models` directory.

**Error Handling**:
- **Model Loading Errors**: Check if `environmental_model.keras` exists in the `models` directory and is accessible.
- **Prediction Errors**: Ensure the input data is in the correct format (a 1D list of numbers).

## Setup and Installation

### Prerequisites
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

### Installation
1. **Navigate to the Backend Directory**:
    ```sh
    cd EcoWatch-RealTime-Environmental-Monitoring/backend
    ```

2. **Install Python Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Backend

1. **Train the Model**:
    ```sh
    python model.py
    ```

2. **Collect Data**:
    ```sh
    python data_collection.py
    ```

3. **Start the Flask API**:
    ```sh
    python app.py
    ```

## Troubleshooting

- **API Issues**:
    - Check API keys and endpoint URLs.
    - Ensure network connectivity and proper API usage limits.

- **Data Handling Issues**:
    - Verify file paths and ensure data files are accessible.
    - Ensure proper data formats in `air_quality.csv` and `weather_data.json`.

- **Flask API Issues**:
    - Ensure the model file path is correct.
    - Check for JSON formatting errors in API requests.