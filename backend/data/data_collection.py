import requests
import pandas as pd
import json
import time
import os
import threading
import keyboard
import signal
import sys

# Constants
AIR_QUALITY_API = "https://api.openaq.org/v2/measurements"
WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather'
WEATHER_API_KEY = "8caeb1304416a17b8525c38c1da89e6f"

# Coordinates for the location you want to get weather data for
latitude = 33.6846
longitude = -117.8265

# Interval to wait between API calls (in seconds)
interval = 10  # 10 seconds

# Number of times to collect data
num_collections = 6  # For example, collect data 6 times

# File to store the weather data
output_file = 'weather_data.json'

# List to store the collected data
weather_data = []

# Flag to stop data collection
stop_flag = threading.Event()


def fetch_air_quality(lat, lon, radius=10000, limit=100, date_from="2024-01-01T00:00:00Z", date_to="2024-07-19T23:59:59Z"):
    headers = {
        'accept': 'application/json'
    }
    params = {
        'coordinates': f'{lat},{lon}',
        'radius': radius,
        'limit': limit,
        'date_from': date_from,
        'date_to': date_to,
        'sort': 'desc'
    }
    try:
        response = requests.get(AIR_QUALITY_API, headers=headers, params=params)
        response.raise_for_status()  # Ensure we catch HTTP errors
        data = response.json()

        if 'results' in data and data['results']:
            df = pd.DataFrame(data['results'])
            df.to_csv('air_quality.csv', index=False)
            print("Air quality data saved.")
        else:
            print("No air quality data found or 'results' key is missing.")
            print("API Response:", data)  # Print the response to debug

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_weather_data(lat, lon, units='metric'):
    url = f"{WEATHER_API}?lat={lat}&lon={lon}&units={units}&appid={WEATHER_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        data = response.json()

        # Check if the response contains the expected data
        if 'main' in data and 'weather' in data:
            print("Weather data received:", data)
            return data
        else:
            print("Unexpected response format:", data)
            return {}

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return {}
    except ValueError as e:
        print(f"JSON decode failed: {e}")
        return {}


def collect_weather_data(num_collections=6, interval=600):
    global weather_data
    for i in range(num_collections):
        if stop_flag.is_set():
            print("Data collection stopped by user.")
            break

        try:
            data = get_weather_data(latitude, longitude)
            if data:
                weather_data.append(data)

                # Save data to a JSON file
                with open(output_file, 'w') as f:
                    json.dump(weather_data, f, indent=4)

                print(f"Data collected and saved at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print("No weather data received.")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for the specified interval before collecting data again
        time.sleep(interval)

    print("Data collection completed.")


def stop_data_collection():
    input("Press 'q' to stop data collection: ")
    stop_flag.set()


def signal_handler(sig, frame):
    print("\nInterrupt signal received. Stopping data collection.")
    stop_flag.set()
    sys.exit(0)


if __name__ == '__main__':
    fetch_air_quality(latitude, longitude)

    # Set up signal handler for graceful exit on Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Start the thread to listen for user input
    input_thread = threading.Thread(target=stop_data_collection, daemon=True)
    input_thread.start()

    # Run the data collection
    collect_weather_data(num_collections=num_collections, interval=interval)

    # Wait for the input thread to finish
    input_thread.join()