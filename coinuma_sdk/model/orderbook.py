from typing import List

from coinuma_sdk.model import Model
from coinuma_sdk.model.orderbook_row import OrderbookRow


class Orderbook(Model):

    def __init__(self, raw_data: dict = None) -> None:
        self._asks: List[OrderbookRow] = []
        self._bids: List[OrderbookRow] = []

        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'asks' in raw_data and raw_data['asks']:
            self.asks = [OrderbookRow(raw_row) for raw_row in raw_data['asks']]
        if 'bids' in raw_data and raw_data['bids']:
            self.bids = [OrderbookRow(raw_row) for raw_row in raw_data['bids']]

    @property
    def asks(self) -> List[OrderbookRow]:
        return self._asks

    @asks.setter
    def asks(self, value: List[OrderbookRow]) -> None:
        assert isinstance(value, list)
        self._asks = value

    @property
    def bids(self) -> List[OrderbookRow]:
        return self._bids

    @bids.setter
    def bids(self, value: List[OrderbookRow]) -> None:
        assert isinstance(value, list)
        self._bids = value
