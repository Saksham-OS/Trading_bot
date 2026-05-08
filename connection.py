from bot import get_client

client = get_client()

print(client.futures_account_balance())