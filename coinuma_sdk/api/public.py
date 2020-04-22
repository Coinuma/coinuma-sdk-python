from typing import List

from coinuma_sdk.api.client import Client
from coinuma_sdk.const import endpoints_public, url_addresses
from coinuma_sdk.model.asset import Asset
from coinuma_sdk.model.orderbook import Orderbook
from coinuma_sdk.model.summary import Summary
from coinuma_sdk.model.symbol import Symbol
from coinuma_sdk.model.trade import Trade
from coinuma_sdk.model.ticker import Ticker


class Public:

    def __init__(self) -> None:
        self._client: Client = Client(url_addresses.PUBLIC)

    def get_summary(self) -> Summary:
        response = self._client.query(endpoints_public.SUMMARY)
        return Summary(response['data'])

    def get_assets(self) -> List[Asset]:
        response = self._client.query(endpoints_public.ASSETS)
        return [Asset(raw_asset) for code, raw_asset in response['data'].items()]

    def get_orderbook(self, symbol: str) -> Orderbook:
        response = self._client.query(endpoints_public.ORDERBOOK.format(symbol=symbol))
        return Orderbook(response['data'])

    def get_trades(self, symbol: str) -> List[Trade]:
        response = self._client.query(endpoints_public.TRADES.format(symbol=symbol))
        return [Trade(raw_trade) for raw_trade in response['data']]

    def get_symbols(self, symbol: str = '') -> List[Symbol]:
        response = self._client.query(endpoints_public.SYMBOLS.format(symbol=symbol))
        return [Symbol(raw_symbol) for raw_symbol in response['data']]

    def get_tickers(self, symbol: str = '') -> List[Ticker]:
        response = self._client.query(endpoints_public.TICKERS.format(symbol=symbol))
        return [Ticker(raw_symbol) for symbol, raw_symbol in response['data'].items()]
