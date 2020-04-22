import datetime
from dateutil import parser
from typing import List

from coinuma_sdk.model import Model
from coinuma_sdk.model.asset import Asset
from coinuma_sdk.model.commissions import Commissions
from coinuma_sdk.model.limits import Limits
from coinuma_sdk.model.ticker import Ticker


class Summary(Model):
    _server_time: datetime.datetime
    _timezone: str
    _commissions: Commissions
    _limits: Limits

    def __init__(self, raw_data: dict = None) -> None:
        self._tickers: List[Ticker] = []
        self._assets: List[Asset] = []

        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'server_time' in raw_data and raw_data['server_time']:
            self.server_time = parser.parse(raw_data['server_time'])
        if 'timezone' in raw_data and raw_data['timezone']:
            self.timezone = raw_data['timezone']
        if 'commissions' in raw_data and raw_data['commissions']:
            self.commissions = Commissions(raw_data['commissions'])
        if 'limits' in raw_data and raw_data['limits']:
            self.limits = Limits(raw_data['limits'])
        if 'tickers' in raw_data and raw_data['tickers']:
            self.tickers = [Ticker(raw_ticker) for raw_ticker in raw_data['tickers']]
        if 'assets' in raw_data and raw_data['assets']:
            self.assets = [Asset(raw_asset) for raw_asset in raw_data['assets']]

    @property
    def server_time(self) -> datetime.datetime:
        return self._server_time

    @server_time.setter
    def server_time(self, value: datetime.datetime) -> None:
        assert isinstance(value, datetime.datetime)
        self._server_time = value

    @property
    def timezone(self) -> str:
        return self._timezone

    @timezone.setter
    def timezone(self, value: str) -> None:
        assert isinstance(value, str)
        self._timezone = value

    @property
    def commissions(self) -> Commissions:
        return self._commissions

    @commissions.setter
    def commissions(self, value: Commissions) -> None:
        assert isinstance(value, Commissions)
        self._commissions = value

    @property
    def limits(self) -> Limits:
        return self._limits

    @limits.setter
    def limits(self, value: Limits) -> None:
        assert isinstance(value, Limits)
        self._limits = value

    @property
    def tickers(self) -> List[Ticker]:
        return self._tickers

    @tickers.setter
    def tickers(self, value: List[Ticker]) -> None:
        assert isinstance(value, list)
        self._tickers = value

    @property
    def assets(self) -> List[Asset]:
        return self._assets

    @assets.setter
    def assets(self, value: List[Asset]) -> None:
        assert isinstance(value, list)
        self._assets = value
