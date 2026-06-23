import os

# Default city to run the pipeline for if none is provided
CITY = os.getenv("CITY", "New York")

# PostgreSQL connection string (must be set in environment variables)
DATABASE_URL = os.getenv("DATABASE_URL")

# Timeout for API requests (seconds)
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "10"))

# Number of retry attempts for API calls before failing
RETRY_COUNT = int(os.getenv("RETRY_COUNT", "3"))