# Stock Matching Engine

The Stock Matching Engine is a Python application that simulates a basic stock exchange. It allows users to place buy and sell orders for two stocks: TATA and RELIANCE. The matching engine matches buy and sell orders based on price and quantity, executing trades when there is a match.

## Prerequisites

- Python 3.x

## Installation

1. **Clone the repository:**
https://github.com/JunaidRafique69/SportHedge
2. **Navigate to the project directory:**
cd SportHedge
3. 
## Usage

To run the matching engine, use the following command:

python main.py

## How It Works

### Matching Logic

- **Buy Orders**: When a buy order is added, the system attempts to match it with existing sell orders. If a match is found (based on price and quantity), a trade is executed, and the sell order(s) are updated or removed.
  
- **Sell Orders**: When a sell order is added, the system attempts to match it with existing buy orders. If a match is found (based on price and quantity), a trade is executed, and the buy order(s) are updated or removed.

- **Partial Fills**: The system handles partial fills by combining multiple orders to fulfill the trade when a perfect match is not found.

### Order Matching Process

1. **Buy Order Addition**: When a buy order is added, the matching engine checks existing sell orders for a match. If no perfect match is found, the engine combines multiple sell orders to fulfill the trade. If a partial or complete match occurs, the trade is executed.

2. **Sell Order Addition**: When a sell order is added, the matching engine checks existing buy orders for a match. If no perfect match is found, the engine combines multiple buy orders to fulfill the trade. If a partial or complete match occurs, the trade is executed.

## Sample Usage

```python
matching_engine = MatchingEngine()

# Adding sample buy and sell orders
matching_engine.add_order("TATA", "buy", 70, 7)
matching_engine.add_order("TATA", "sell", 60, 6)
matching_engine.add_order("TATA", "sell", 20, 2)

# Display order books
matching_engine.display_order_book("TATA")
