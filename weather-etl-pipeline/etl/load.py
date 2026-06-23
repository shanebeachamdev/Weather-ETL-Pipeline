import os
from sqlalchemy import create_engine

def load_to_postgres(df, table_name="weather_data"):
    """
    Loads transformed DataFrame into a PostgreSQL table.

    Uses environment variable for secure database connection.
    """

    # Fetch database connection string from environment
    db_url = os.getenv("DATABASE_URL")

    if not db_url:
        raise ValueError("DATABASE_URL environment variable not set")

    # Create SQLAlchemy engine
    engine = create_engine(db_url)

    # Append data into existing table
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )