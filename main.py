class Order:
    """Represents a buy or sell order for a stock.

    Attributes:
        price (float): The price of the order.
        quantity (int): The quantity of shares in the order.
        order_type (str): Type of the order, 'buy' or 'sell'.
    """

    def __init__(self, price, quantity, order_type):
        """Initializes an Order object with the given price, quantity, and order type."""
        self.price = price
        self.quantity = quantity
        self.order_type = order_type

    def __str__(self):
        """Returns a formatted string representation of the Order object."""
        return f"Type: {self.order_type}, Price: {self.price}, Quantity: {self.quantity}"


class Stock:
    """Represents a stock with its buy and sell orders.

    Attributes:
        name (str): The name of the stock.
        buy_orders (list): List to store buy orders.
        sell_orders (list): List to store sell orders.
    """

    def __init__(self, name):
        """Initializes a Stock object with the given name and empty order lists."""
        self.name = name
        self.buy_orders = []  # List to store buy orders
        self.sell_orders = []  # List to store sell orders

    def add_order(self, order):
        """Adds a buy or sell order to the stock's order list.

        Args:
            order (Order): The order object to be added.
        """
        if order.order_type == 'buy':
            self.buy_orders.append(order)
            self.buy_orders.sort(key=lambda x: x.price, reverse=True)  # Sort buy orders by price descending
        elif order.order_type == 'sell':
            self.sell_orders.append(order)
            self.sell_orders.sort(key=lambda x: x.price)  # Sort sell orders by price ascending

    def __str__(self):
        """Returns a formatted string representation of the Stock object."""
        buy_orders_info = "\n".join(str(order) for order in self.buy_orders)
        sell_orders_info = "\n".join(str(order) for order in self.sell_orders)
        return f"Stock: {self.name}\nBuy Orders:\n{buy_orders_info}\nSell Orders:\n{sell_orders_info}"



class MatchingEngine:
    """Implements a matching engine for stock trading.

    Attributes:
        stocks (dict): Dictionary to store Stock objects with stock names as keys.
    """

    def __init__(self):
        """Initializes a MatchingEngine object with an empty dictionary to store stocks."""
        self.stocks = {"TATA": Stock("TATA"), "RELIANCE": Stock("RELIANCE")}

    def add_order(self, stock_name, order_type, price, quantity):
        """Adds a buy or sell order to the specified stock and matches orders if possible.

        Args:
            stock_name (str): The name of the stock (TATA or RELIANCE).
            order_type (str): Type of the order, 'buy' or 'sell'.
            price (float): The price of the order.
            quantity (int): The quantity of shares in the order.
        """
        if stock_name not in self.stocks:
            print(f"Invalid stock name: {stock_name}")
            return

        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity")
            return

        order = Order(price, quantity, order_type)
        stock = self.stocks[stock_name]
        if order_type == 'sell':
            self.match_sell_order(stock, order)
        elif order_type == 'buy':
            self.match_buy_order(stock, order)

    def match_sell_order(self, stock, sell_order):
        """Matches a sell order with buy orders and updates the buy orders list accordingly.

        Args:
            stock (Stock): The stock object.
            sell_order (Order): The sell order to be matched.
        """
        # Iterate through buy orders and find matches
        for buy_order in stock.buy_orders:
            if buy_order.price >= sell_order.price and buy_order.quantity > 0 and sell_order.quantity > 0:
                matched_quantity = min(buy_order.quantity, sell_order.quantity)
                print(f"Matched {matched_quantity} shares at price {buy_order.price}")
                buy_order.quantity -= matched_quantity
                sell_order.quantity -= matched_quantity
                if buy_order.quantity == 0:
                    stock.buy_orders.remove(buy_order)
                if sell_order.quantity == 0:
                    return  # Sell order fulfilled
        # If the sell order is not fulfilled, add it to the sell orders list
        stock.sell_orders.append(sell_order)

    def match_buy_order(self, stock, buy_order):
        """Matches a buy order with sell orders and updates the sell orders list accordingly.

        Args:
            stock (Stock): The stock object.
            buy_order (Order): The buy order to be matched.
        """
        # Iterate through sell orders and find matches
        for sell_order in stock.sell_orders:
            if sell_order.price <= buy_order.price and buy_order.quantity > 0 and sell_order.quantity > 0:
                matched_quantity = min(buy_order.quantity, sell_order.quantity)
                print(f"Matched {matched_quantity} shares at price {sell_order.price}")
                buy_order.quantity -= matched_quantity
                sell_order.quantity -= matched_quantity
                if sell_order.quantity == 0:
                    stock.sell_orders.remove(sell_order)
                if buy_order.quantity == 0:
                    return  # Buy order fulfilled
        # If the buy order is not fulfilled, add it to the buy orders list
        stock.buy_orders.append(buy_order)

    def display_order_book(self, stock_name):
        """Displays the order book for the specified stock.

        Args:
            stock_name (str): The name of the stock (TATA or RELIANCE).
        """
        if stock_name not in self.stocks:
            print(f"Invalid stock name: {stock_name}")
            return
        stock = self.stocks[stock_name]
        print(stock)


# Sample usage and testing
matching_engine = MatchingEngine()

# Adding sample buy and sell orders
matching_engine.add_order("TATA", "buy", 155, 5)
matching_engine.add_order("TATA", "sell", 160, 7)
matching_engine.add_order("TATA", "sell", 155, 5)
matching_engine.add_order("TATA", "buy", 160, 7)
matching_engine.add_order("RELIANCE", "sell", 200, 10)
matching_engine.add_order("RELIANCE", "buy", 190, 8)
matching_engine.add_order("RELIANCE", "sell", 190, 7)

# Display order books
matching_engine.display_order_book("TATA")
matching_engine.display_order_book("RELIANCE")

# Handling edge cases
matching_engine.add_order("InvalidStock", "buy", 150, 5)  # Invalid stock name
matching_engine.add_order("TATA", "buy", -1, 5)  # Invalid price
matching_engine.add_order("TATA", "buy", 150, -5)  # Invalid quantity
