from sqlalchemy import create_engine
from schema import create_all_tables
from dotenv import load_dotenv
import os

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get the database URL from environment variables
    database_url = os.getenv('DATABASE_URL')
    if database_url is None:
        raise ValueError("DATABASE_URL not found in .env file.")

    # Create engine with the database URL
    engine = create_engine(database_url)
    create_all_tables(engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    main()
