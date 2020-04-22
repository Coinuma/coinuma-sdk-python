from decimal import Decimal

from coinuma_sdk.model import Model


class Commissions(Model):
    _maker: Decimal
    _taker: Decimal

    def __init__(self, raw_data: dict = None) -> None:
        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'maker' in raw_data and raw_data['maker']:
            self.maker = Decimal(raw_data['maker'])
        if 'taker' in raw_data and raw_data['taker']:
            self.taker = Decimal(raw_data['taker'])

    @property
    def maker(self) -> Decimal:
        return self._maker

    @maker.setter
    def maker(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._maker = value

    @property
    def taker(self) -> Decimal:
        return self._taker

    @taker.setter
    def taker(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._taker = value
