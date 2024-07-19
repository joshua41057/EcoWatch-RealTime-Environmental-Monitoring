from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from models import model  # import my model

app = Flask(__name__)
CORS(app)  # enable cors


@app.route('/api/data', methods=['GET'])
def get_data():
    # Implement data fetching logic
    return jsonify({'message': 'Data fetched successfully'})


@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    # Preprocess data and run model prediction
    result = model.predict(data)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
