# Fetch weather data from OpenWeatherMap API

import requests

API_KEY = '60ed420050f5ec13c31bb39f88771a50'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city, state):
    location = f"{city},{state},US"
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return None

def display_weather(data):
    if data:
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("No data to display.")

def main():
    location = input("Enter the city name followed by a comma and the state abbreviation (e.g., 'Los Angeles,CA'): ")
    try:
        city, state = [x.strip() for x in location.split(',')]
        weather_data = get_weather(city, state)
        display_weather(weather_data)
    except ValueError:
        print("Invalid input format. Please enter the city name followed by a comma and the state abbreviation.")

if __name__ == "__main__":
    main()