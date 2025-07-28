from dotenv import load_dotenv
import os

load_dotenv()

db_login = os.getenv('DB_LOGIN')
db_senha = os.getenv('DB_SENHA')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}