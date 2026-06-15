# backend/utils/weather_tool.py
import os
import requests
from dotenv import load_dotenv

# Load key variables straight from your secure .env file
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def fetch_live_weather(city_name: str):
    """
    Connects to the WeatherAPI service using a secure key to retrieve
    real-time climate metrics for dynamic plant disease analysis.
    """
    if not API_KEY:
        return {"error": "WEATHER_API_KEY is missing from your .env configuration file."}

    # WeatherAPI current weather endpoint
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": API_KEY,
        "q": city_name,
        "aqi": "no"  # We don't need air quality data for the crops
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        
        # Handle wrong city names or invalid keys cleanly
        if response.status_code != 200:
            return {"error": f"API request failed with status code {response.status_code}. Check your city name or key."}
            
        data = response.json()
        current = data.get("current", {})
        location = data.get("location", {})
        
        # Package the metrics neatly for our orchestrator
        climate_payload = {
            "city": f"{location.get('name')}, {location.get('country')}",
            "temperature_celsius": current.get("temp_c"),
            "humidity_percentage": current.get("humidity"),
            "weather_condition": current.get("condition", {}).get("text"),
            "wind_speed_kmh": current.get("wind_kph")
        }
        return climate_payload

    except Exception as e:
        return {"error": f"Weather lookup failed due to network exception: {str(e)}"}
