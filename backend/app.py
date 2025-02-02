from flask import Flask, jsonify, request
from flask_cors import CORS
import tensorflow as tf
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the weather data JSON file
weather_data_path = 'data/weather_data.json'  # Update this path


def load_model():
    try:
        model = tf.keras.models.load_model('models/environmental_model.keras')
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise


app_model = load_model()


@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # Read the weather data from the file
        with open(weather_data_path, 'r') as file:
            weather_data = file.read()
        return weather_data, 200, {'Content-Type': 'application/json'}
    except Exception as e:
        print(f"Error reading weather data: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Check if request contains 'data'
        if not request.json or 'data' not in request.json:
            return jsonify({'error': 'No data provided'}), 400

        # Get the data and reshape it
        data = request.json['data']
        if not isinstance(data, list):
            return jsonify({'error': 'Data should be a list'}), 400

        data = np.array(data, dtype=np.float32)  # Ensure data is float32
        if len(data.shape) != 1:
            return jsonify({'error': 'Data should be a 1D list'}), 400

        data = data.reshape((1, len(data), 1))  # Reshape data for model input
        prediction = app_model.predict(data)
        return jsonify(prediction.tolist())
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/weather', methods=['GET'])
def get_weather():
    try:
        # Example of static weather data; replace with actual data fetching logic
        weather_data = {
            'temperature': 72,
            'humidity': 50,
            'condition': 'Clear'
        }
        return jsonify(weather_data)
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
