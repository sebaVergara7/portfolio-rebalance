"""
Unit tests for the Portfolio class

This file validates that the portfolio_value method correctly calculates
the total value of a portfolio given stock quantities and current prices.
"""

from src.stock import Stock
from src.portfolio import Portfolio


def test_portfolio_value():
    """
    Test that portfolio_value returns the correct total.

    Creates a portfolio with META and AAPL stocks, assigns fixed prices,
    and verifies that the computed portfolio value matches the expected
    manual calculation.
    """
    META_ALLOCATION = 0.4
    AAPL_ALLOCATION = 0.6

    META_STOCKS = 10
    AAPL_STOCKS = 50

    META_STOCK_PRICE = 500
    AAPL_STOCK_PRICE = 200

    # Simulated market data
    market_data = {
        "META": Stock("META", META_STOCK_PRICE),
        "AAPL": Stock("AAPL", AAPL_STOCK_PRICE),
    }

    # Portfolio instance
    portfolio = Portfolio(
        stocks={"META": META_STOCKS, "AAPL": AAPL_STOCKS},
        allocation={"META": META_ALLOCATION, "AAPL": AAPL_ALLOCATION},
        market=market_data,
    )

    # Expected manual calculation
    expected_value = META_STOCKS * META_STOCK_PRICE + AAPL_STOCKS * AAPL_STOCK_PRICE

    # Assertion
    assert portfolio.portfolio_value() == expected_value
