CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    temperature_C FLOAT,
    humidity INT,
    weather_desc TEXT,
    wind_speed_kmph FLOAT,
);