import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_current_weather(city="Islamabad"):
    api_key = os.getenv("API_KEY")

    if not api_key:
        return None  # Fail early if no API key

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        return response.json()
    except Exception:
        return None
