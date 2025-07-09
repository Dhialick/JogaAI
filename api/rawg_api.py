import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("rawg_api_key")
base_url = "https://api.rawg.io/api"

def get_games(search=None):
    url = f"{base_url}/games"