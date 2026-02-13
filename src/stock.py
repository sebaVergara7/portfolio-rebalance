from typing import Dict, List


class Stock:
    def __init__(self, symbol: str, current_price: float):
        self.symbol = symbol
        self.current_price = current_price

    def get_current_price(self) -> float:
        return self.current_price
