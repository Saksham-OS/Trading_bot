from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_CODE")

client = Client(api_key, api_secret)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

def get_client():
    return client