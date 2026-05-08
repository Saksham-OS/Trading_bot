import argparse
from colorama import Fore, init

from orders import (
    place_market_order,
    place_limit_order,
    print_order_summary,
    print_order_response
)

from validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from logging_config import logger

init(autoreset=True)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Price for LIMIT order")

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        if order_type == "MARKET":
            response = place_market_order(symbol, side, quantity)
        else:
            response = place_limit_order(symbol, side, quantity, price)

        print_order_summary(symbol, side, order_type, quantity, price, response)
        print_order_response(response)
        print(Fore.GREEN + "SUCCESS: Order placed successfully")

    except ValueError as e:
        logger.error(f"Validation Error: {e}")
        print(Fore.RED + f"Validation Error: {e}")

    except Exception as e:
        logger.error(f"Application Error: {e}")
        print(Fore.RED + f"Application Error: {e}")


if __name__ == "__main__":
    main()
