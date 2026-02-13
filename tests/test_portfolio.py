from src.stock import Stock
from src.portfolio import Portfolio


def test_portfolio_value():
    META_ALLOCATION = 0.4
    AAPL_ALLOCATION = 0.6

    META_STOCKS = 10
    AAPL_STOCKS = 50

    META_STOCK_PRICE = 500
    AAPL_STOCK_PRICE = 200

    market_data = {
        "META": Stock("META", META_STOCK_PRICE),
        "AAPL": Stock("AAPL", AAPL_STOCK_PRICE),
    }

    portfolio = Portfolio(
        stocks={"META": META_STOCKS, "AAPL": AAPL_STOCKS},
        allocation={"META": META_ALLOCATION, "AAPL": AAPL_ALLOCATION},
        market=market_data,
    )

    expected_value = META_STOCKS * META_STOCK_PRICE + AAPL_STOCKS * AAPL_STOCK_PRICE

    assert portfolio.portfolio_value() == expected_value
