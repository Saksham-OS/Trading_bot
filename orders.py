from binance.exceptions import BinanceAPIException
from bot import get_client
from logging_config import logger

client = get_client()


def print_order_summary(symbol, side, order_type, quantity, price=None, response=None):
    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol      : {symbol}")
    print(f"Side        : {side}")
    print(f"Order Type  : {order_type}")
    print(f"Quantity    : {quantity}")

    if price:
        print(f"Price       : {price}")

    if response:
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")

        avg_price = response.get('avgPrice')
        if avg_price:
            print(f"Average Price: {avg_price}")

    print("====================================\n")

def print_order_response(response):
    print("========== ORDER RESPONSE ==========")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print("====================================\n")



def place_market_order(symbol, side, quantity):
    try:
        logger.info(
            f"MARKET ORDER REQUEST | Symbol={symbol} Side={side} Quantity={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"MARKET ORDER RESPONSE | {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise

def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"LIMIT ORDER REQUEST | Symbol={symbol} Side={side} Quantity={quantity} Price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"LIMIT ORDER RESPONSE | {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise
        