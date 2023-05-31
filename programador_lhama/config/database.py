import os

from dotenv import load_dotenv

load_dotenv()

database_info = {
    "database": os.getenv('DATABASE'),
    "port": os.getenv('PORT'),
    "user": os.getenv('USER'),
    "password": os.getenv('PASSWORD')
}