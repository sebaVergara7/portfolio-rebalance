from typing import Dict, List


class Stock:
    """
    Stock class

    Represents a single stock with its symbol and current price.
    This class is the basic building block for portfolio calculations.
    """

    def __init__(self, symbol: str, current_price: float):
        """
        Initialize a Stock instance.

        Args:
            symbol (str): The ticker symbol of the stock (e.g., "AAPL").
            current_price (float): The current market price of the stock.
        """
        self.symbol = symbol
        self.current_price = current_price

    def get_current_price(self) -> float:
        """
        Retrieve the current price of the stock.

        Returns:
            float: The current market price of the stock.
        """
        return self.current_price
