"""
Basic usage example

This script demonstrates how to use the Stock and Portfolio classes.
It creates a simple portfolio with two stocks (META and AAPL),
calculates the total portfolio value, and prints the dollar adjustments
needed to rebalance according to the target allocation.
"""

from src.stock import Stock
from src.portfolio import Portfolio

if __name__ == "__main__":
    # Simulated market data
    market_data = {
        "META": Stock("META", 500),
        "AAPL": Stock("AAPL", 200),
    }

    # Portfolio with current holdings and target allocation
    portfolio = Portfolio(
        stocks={"META": 10, "AAPL": 50},
        allocation={"META": 0.4, "AAPL": 0.6},
        market=market_data,
    )

    # Output results
    print("Total portfolio value:", portfolio.portfolio_value())
    print("Actions needed to rebalance (in dollars):", portfolio.rebalance())
