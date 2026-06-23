# Weather ETL Pipeline
A modular Python-based ETL (Extract, Transform, Load) pipeline that retrieves real-time weather data from an external API, transforms it into structured format, and loads it into a PostgreSQL database for storage and analysis.

# Overview
This project demonstrates a clean ETL workflow commonly used in data engineering pipelines:

Extract: Fetches live weather data from the wttr.in API
Transform: Processes and structures raw JSON data using Pandas
Load: Stores cleaned data into a PostgreSQL database

The pipeline is designed with modularity, logging, and configuration best practices to simulate a production-style data ingestion system.

# Architecture
Weather API (wttr.in)
        ↓
   Extract Layer (requests + retry logic)
        ↓
   Transform Layer (pandas processing)
        ↓
   Load Layer (PostgreSQL via SQLAlchemy)
        ↓
   weather_data table

# Tech Stack
Python 3.x
Requests
Pandas
SQLAlchemy
PostgreSQL
Logging (built-in Python logging module)

# Project Structure
weather-etl-pipeline/
│
├── etl/
│   ├── extract.py        # Fetches weather data from API
│   ├── transform.py      # Cleans and structures data
│   ├── load.py           # Loads data into PostgreSQL
│   └── pipeline.py       # Orchestrates ETL workflow
│
├── config/
│   └── config.py         # Environment-based configuration
│
├── sql/
│   └── create_tables.sql # Database schema definition
│
├── logs/
│   └── log.py            # Logging configuration utility
│
├── run_pipeline.py       # Application entry point
├── requirements.txt
└── README.md

# Getting Started
1. Clone the repository
git clone https://github.com/your-username/weather-etl-pipeline.git
cd weather-etl-pipeline
2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

This project uses environment variables for configuration.

Example (Mac/Linux):
export DATABASE_URL="postgresql://user:password@localhost:5432/weather_db"
export CITY="New York"
Example (Windows PowerShell):
setx DATABASE_URL "postgresql://user:password@localhost:5432/weather_db"
setx CITY "New York"

# Database Setup
Run the SQL script to create the required table:

psql -U postgres -d weather_db -f sql/create_tables.sql

# Running the Pipeline
Execute the ETL pipeline:

python run_pipeline.py

# Output Schema
Data is stored in the weather_data table:

Column	Type	Description
id	SERIAL	Primary key
temperature_C	FLOAT	Current temperature
humidity	INT	Humidity percentage
weather_desc	TEXT	Weather condition
wind_speed_kmph	FLOAT	Wind speed
created_at	TIMESTAMP	Record insertion time

# Example Workflow
Fetch weather data from API
Retry automatically if request fails
Transform nested JSON into structured format
Validate and convert data types
Insert into PostgreSQL table
Log each step of the pipeline

# Key Features
Modular ETL architecture (separation of concerns)
Real-time API integration
Retry logic with timeout handling
Environment-based configuration (no hardcoded secrets)
Structured logging system
PostgreSQL integration using SQLAlchemy
Clean, production-style pipeline orchestration

# Future Improvements
Potential enhancements for production-level expansion:

Add multi-city batch processing
Containerize with Docker
Schedule pipeline runs (cron / Airflow)
Add unit tests for ETL components
Build dashboard for visualizing stored weather data

# Author
Shane Beacham
GitHub: [https://github.com/shanebeachamdev]

# License
This project is open-source and available under the MIT License.
