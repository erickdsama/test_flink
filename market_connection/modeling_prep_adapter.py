import os

import requests

from market_connection.abstract_market_repository import AbstractMarketRepository
from market_connection.exceptions import WrongCompanySymbol


class ModelingPrepAdapter(AbstractMarketRepository):
    def __init__(self):
        self.url = 'https://financialmodelingprep.com/api/v3/'
        self.api_key = os.getenv('financial_api_key')

    def verify_company_symbol(self, symbol: str) -> list:
        method = 'enterprise-values/'
        url = f'{self.url}{method}{symbol}?apikey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 404:
            raise WrongCompanySymbol(f'Company symbol: {symbol} does not exist')
        values = response.json()
        if not values:
            raise WrongCompanySymbol(f'Company symbol: {symbol} does not exist')

        return values

    def get_market_values(self, symbol: str):
        values = self.verify_company_symbol(symbol=symbol)
        for value in values:
            yield value.get('enterpriseValue', 0.0)
