"""
Basic usage
"""

from src.stock import Stock
from src.portfolio import Portfolio

if __name__ == "__main__":
    market_data = {
        "META": Stock("META", 500),
        "AAPL": Stock("AAPL", 200),
    }

    portfolio = Portfolio(
        stocks={"META": 10, "AAPL": 50},
        allocation={"META": 0.4, "AAPL": 0.6},
        market=market_data,
    )

    print("Total portfolio value:", portfolio.portfolio_value())
    print("Actions needed to rebalance (in dollars):", portfolio.rebalance())
