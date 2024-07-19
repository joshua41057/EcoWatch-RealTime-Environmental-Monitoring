import tensorflow as tf
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Dense, LSTM
import pandas as pd
import numpy as np

def create_model():
    model = Sequential()
    model.add(Input(shape=(None, 1)))  # Use Input layer for shape specification
    model.add(LSTM(50, return_sequences=True))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_model():
    # Load and preprocess data
    df = pd.read_csv('../data/air_quality.csv')  # Adjusted path

    # Example preprocessing
    df = df[['value']].fillna(method='ffill')  # Fill missing values
    X = df.values
    y = np.roll(X, -1, axis=0)  # Shift data for prediction

    # Remove last row for y to match X
    X_train, y_train = X[:-1], y[1:]

    model = create_model()
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    model.save('environmental_model.keras')  # Save model in native Keras format

def predict(data):
    model = tf.keras.models.load_model('environmental_model.keras')
    # Ensure data is in the right shape for prediction
    data = np.array(data).reshape((1, len(data), 1))
    prediction = model.predict(data)
    return prediction

if __name__ == "__main__":
    train_model()
