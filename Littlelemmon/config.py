import os
from dotenv import load_dotenv


load_dotenv()


def get_db_details():

    db_data = {
        "NAME": os.environ.get("DB_NAME"),
        "USERNAME": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),  
    }
    return db_data