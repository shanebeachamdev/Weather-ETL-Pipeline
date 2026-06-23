import pandas as pd

def transform_weather(data):
    """
    Transforms raw weather API response into structured tabular format.

    Extracts key fields needed for database storage and reporting.
    """

    current = data["current_condition"][0]

    # Convert nested JSON into a structured DataFrame row
    df = pd.DataFrame([{
        "temperature_C": float(current.get("temp_C", 0)),
        "humidity": int(current.get("humidity", 0)),
        "weather_desc": current["weatherDesc"][0]["value"],
        "wind_speed_kmph": float(current.get("windspeedKmph", 0))
    }])

    return df