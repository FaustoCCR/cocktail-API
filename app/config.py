from pydantic.v1 import BaseSettings
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Settings(BaseSettings):
    mongodb_url = os.getenv("MONGODB_CONNECTION_STRING")
