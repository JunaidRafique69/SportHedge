# Stock Matching Engine

This project implements a simple matching engine for stock trading. The engine matches buy and sell orders for two types of stocks: TATA and RELIANCE based on the quoted prices.

## Classes

### Stock
- Represents a stock with its buy and sell orders.
- Methods:
  - `add_order(order)`: Adds a buy or sell order to the stock.

### Order
- Represents a buy or sell order with a specific price and quantity.
- Attributes:
  - `price`: Price of the order.
  - `quantity`: Quantity of shares in the order.
  - `order_type`: Type of the order ('buy' or 'sell').

### MatchingEngine
- Implements the logic to match buy and sell orders for different stocks.
- Methods:
  - `add_order(stock_name, order_type, price, quantity)`: Adds a buy or sell order to the specified stock.
  - `match_orders(stock_name)`: Matches buy and sell orders for the given stock.
  - `display_order_book(stock_name)`: Displays the order book for the specified stock.

## Usage

1. Install the required packages: `pip install -r requirements.txt`
2. Run the matching engine script: `python matching_engine.py`

## Sample Usage

```python
# Sample usage of the matching engine
matching_engine = MatchingEngine()

# Adding sample buy and sell orders
matching_engine.add_order("TATA", "buy", 155, 5)
matching_engine.add_order("TATA", "sell", 160, 7)
matching_engine.add_order("RELIANCE", "sell", 200, 10)
matching_engine.add_order("RELIANCE", "buy", 190, 8)

# Display order books
matching_engine.display_order_book("TATA")
matching_engine.display_order_book("RELIANCE")
