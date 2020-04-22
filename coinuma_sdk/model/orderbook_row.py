from decimal import Decimal

from coinuma_sdk.model import Model


class OrderbookRow(Model):
    _price: Decimal
    _volume: Decimal

    def __init__(self, raw_data: dict = None) -> None:
        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'price' in raw_data and raw_data['price']:
            self.price = Decimal(raw_data['price'])
        if 'volume' in raw_data and raw_data['volume']:
            self.volume = Decimal(raw_data['volume'])

    @property
    def price(self) -> Decimal:
        return self._price

    @price.setter
    def price(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._price = value

    @property
    def volume(self) -> Decimal:
        return self._volume

    @volume.setter
    def volume(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._volume = value
