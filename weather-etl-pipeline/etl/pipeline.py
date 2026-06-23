from etl.extract import extract_weather
from etl.transform import transform_weather
from etl.load import load_to_postgres
from logs.log import get_logger
from config.config import CITY

# Initialize logger for pipeline tracking
logger = get_logger()

def run_pipeline(city=CITY):
    """
    Main ETL orchestration function.

    Executes the full pipeline:
    Extract → Transform → Load
    """

    try:
        logger.info(f"Pipeline started for city: {city}")

        # Step 1: Extract raw weather data
        raw_data = extract_weather(city)
        logger.info("Data extraction completed")

        # Step 2: Transform raw data into structured format
        clean_data = transform_weather(raw_data)
        logger.info("Data transformation completed")

        # Step 3: Load structured data into PostgreSQL
        load_to_postgres(clean_data)
        logger.info("Data load completed")

        logger.info("Pipeline completed successfully")

    except Exception as e:
        # Log full failure for debugging purposes
        logger.error(f"Pipeline failed: {e}")
        raise