from typing import Dict, List
from src.stock import Stock


class Portfolio:
    """
    Portfolio class Represents an investment portfolio composed of multiple stocks.
    It stores the number of shares held, the target allocation, and
    the current market data for each stock.
    """

    def __init__(
        self,
        stocks: Dict[str, int],
        allocation: Dict[str, float],
        market: Dict[str, Stock],
    ):
        """
        Initialize a Portfolio instance.

        Args:
            stocks (Dict[str, int]): Dictionary mapping stock symbols to number of shares.
            allocation (Dict[str, float]): Target allocation percentages for each stock.
            market (Dict[str, Stock]): Market data containing Stock objects with current prices.
        """
        self.stocks = stocks
        self.allocation = allocation
        self.market = market

    def portfolio_value(self) -> float:
        """
        Calculate the total value of the portfolio.

        Returns:
            float: The sum of shares multiplied by their current prices.
        """
        return sum(
            self.stocks[symbol] * self.market[symbol].get_current_price()
            for symbol in self.stocks
        )

    def rebalance(self) -> Dict[str, float]:
        """
        Calculate the dollar adjustments needed to match the target allocation.

        Returns:
            Dict[str, float]: A dictionary mapping stock symbols to the amount
            (positive = buy, negative = sell) required to reach the target allocation.
        """
        total_value = self.portfolio_value()
        target_values = {
            symbol: total_value * self.allocation[symbol] for symbol in self.allocation
        }

        current_values = {
            symbol: self.stocks.get(symbol, 0) * self.market[symbol].get_current_price()
            for symbol in self.allocation
        }

        rebalance_actions = {
            symbol: target_values[symbol] - current_values[symbol]
            for symbol in self.allocation
        }

        return rebalance_actions
