from typing import Dict, List
from src.stock import Stock


class Portfolio:
    def __init__(
        self,
        stocks: Dict[str, int],
        allocation: Dict[str, float],
        market: Dict[str, Stock],
    ):
        self.stocks = stocks
        self.allocation = allocation
        self.market = market

    def portfolio_value(self) -> float:
        return sum(
            self.stocks[symbol] * self.market[symbol].get_current_price()
            for symbol in self.stocks
        )

    def rebalance(self) -> Dict[str, float]:
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
