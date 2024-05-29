import dotenv
import os
import sqlite3

connection = sqlite3.connect('app/database.db', check_same_thread=False)
dotenv.load_dotenv()

REPLICATE_API_KEY = str(os.getenv("REPLICATE_API_KEY"))