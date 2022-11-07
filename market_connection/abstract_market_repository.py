from abc import ABC, abstractmethod


class AbstractMarketRepository(ABC):

    @abstractmethod
    def verify_company_symbol(self, symbol: str):
        ...

    @abstractmethod
    def get_market_values(self, symbol: str):
        ...
