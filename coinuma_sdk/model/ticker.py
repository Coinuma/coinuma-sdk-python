import datetime
from decimal import Decimal

from dateutil import parser

from coinuma_sdk.model import Model
from coinuma_sdk.model.asset import Asset


class Ticker(Model):
    _symbol: str
    _asset_base: Asset
    _asset_quote: Asset
    _last: Decimal
    _high: Decimal
    _low: Decimal
    _open: Decimal
    _price_average: Decimal
    _ask: Decimal
    _bid: Decimal
    _price_change: Decimal
    _price_change_percent: Decimal
    _volume: Decimal
    _total_transactions: int
    _last_trade_timestamp: datetime.datetime
    _last_trade_direction: str

    def __init__(self, raw_data: dict) -> None:
        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'symbol' in raw_data and raw_data['symbol']:
            self.symbol = raw_data['symbol']
        if 'asset_base' in raw_data and raw_data['asset_base']:
            self.asset_base = Asset(raw_data['asset_base'])
        if 'asset_quote' in raw_data and raw_data['asset_quote']:
            self.asset_quote = Asset(raw_data['asset_quote'])
        if 'last' in raw_data and raw_data['last']:
            self.last = Decimal(raw_data['last'])
        if 'high' in raw_data and raw_data['high']:
            self.high = Decimal(raw_data['high'])
        if 'low' in raw_data and raw_data['low']:
            self.low = Decimal(raw_data['low'])
        if 'open' in raw_data and raw_data['open']:
            self.open = Decimal(raw_data['open'])
        if 'price_average' in raw_data and raw_data['price_average']:
            self.price_average = Decimal(raw_data['price_average'])
        if 'ask' in raw_data and raw_data['ask']:
            self.ask = Decimal(raw_data['ask'])
        if 'bid' in raw_data and raw_data['bid']:
            self.bid = Decimal(raw_data['bid'])
        if 'price_change' in raw_data and raw_data['price_change']:
            self.price_change = Decimal(raw_data['price_change'])
        if 'price_change_percent' in raw_data and raw_data['price_change_percent']:
            self.price_change_percent = Decimal(raw_data['price_change_percent'])
        if 'volume' in raw_data and raw_data['volume']:
            self.volume = Decimal(raw_data['volume'])
        if 'total_transactions' in raw_data and raw_data['total_transactions']:
            self.total_transactions = raw_data['total_transactions']
        if 'last_trade_timestamp' in raw_data and raw_data['last_trade_timestamp']:
            self.last_trade_timestamp = parser.parse(raw_data['last_trade_timestamp'])
        if 'last_trade_direction' in raw_data and raw_data['last_trade_direction']:
            self.last_trade_direction = raw_data['last_trade_direction']

    @property
    def symbol(self) -> str:
        return self._symbol

    @symbol.setter
    def symbol(self, value: str) -> None:
        assert isinstance(value, str)
        self._symbol = value

    @property
    def asset_base(self) -> Asset:
        return self._asset_base

    @asset_base.setter
    def asset_base(self, value: Asset) -> None:
        assert isinstance(value, Asset)
        self._asset_base = value

    @property
    def asset_quote(self) -> Asset:
        return self._asset_quote

    @asset_quote.setter
    def asset_quote(self, value: Asset) -> None:
        assert isinstance(value, Asset)
        self._asset_quote = value

    @property
    def last(self) -> Decimal:
        return self._last

    @last.setter
    def last(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._last = value

    @property
    def high(self) -> Decimal:
        return self._high

    @high.setter
    def high(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._high = value

    @property
    def low(self) -> Decimal:
        return self._low

    @low.setter
    def low(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._low = value

    @property
    def open(self) -> Decimal:
        return self._open

    @open.setter
    def open(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._open = value

    @property
    def price_average(self) -> Decimal:
        return self._price_average

    @price_average.setter
    def price_average(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._price_average = value

    @property
    def ask(self) -> Decimal:
        return self._ask

    @ask.setter
    def ask(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._ask = value

    @property
    def bid(self) -> Decimal:
        return self._bid

    @bid.setter
    def bid(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._bid = value

    @property
    def price_change(self) -> Decimal:
        return self._price_change

    @price_change.setter
    def price_change(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._price_change = value

    @property
    def price_change_percent(self) -> Decimal:
        return self._price_change_percent

    @price_change_percent.setter
    def price_change_percent(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._price_change_percent = value

    @property
    def volume(self) -> Decimal:
        return self._volume

    @volume.setter
    def volume(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._volume = value

    @property
    def total_transactions(self) -> int:
        return self._total_transactions

    @total_transactions.setter
    def total_transactions(self, value: int) -> None:
        assert isinstance(value, int)
        self._total_transactions = value

    @property
    def last_trade_timestamp(self) -> datetime.datetime:
        return self._last_trade_timestamp

    @last_trade_timestamp.setter
    def last_trade_timestamp(self, value: datetime.datetime) -> None:
        assert isinstance(value, datetime.datetime)
        self._last_trade_timestamp = value

    @property
    def last_trade_direction(self) -> str:
        return self._last_trade_direction

    @last_trade_direction.setter
    def last_trade_direction(self, value: str) -> None:
        assert isinstance(value, str)
        self._last_trade_direction = value
