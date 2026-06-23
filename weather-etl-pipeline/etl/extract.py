import requests
from config.config import API_TIMEOUT, RETRY_COUNT

def extract_weather(city="New York"):
    """
    Extracts raw weather data from wttr.in API.

    Includes retry logic and timeout handling to simulate
    real-world API reliability patterns.
    """

    url = f"https://wttr.in/{city}?format=j1"

    # Retry loop in case of temporary API/network failures
    for attempt in range(RETRY_COUNT):
        try:
            response = requests.get(url, timeout=API_TIMEOUT)

            # Raise error for HTTP issues (4xx, 5xx)
            response.raise_for_status()

            # Return raw JSON response
            return response.json()

        except requests.RequestException as e:
            # On final attempt, raise error to stop pipeline
            if attempt == RETRY_COUNT - 1:
                raise Exception(
                    f"Failed to fetch weather data after {RETRY_COUNT} attempts: {e}"
                )