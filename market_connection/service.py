from market_connection.abstract_market_repository import AbstractMarketRepository


class MarketConnectionService:

    def __init__(self, adapter: AbstractMarketRepository):
        self.adapter = adapter

    def verify_symbol(self, symbol: str):
        return self.adapter.verify_company_symbol(symbol=symbol)

    def get_market_values(self, symbol: str):
        return self.adapter.get_market_values(symbol=symbol)
