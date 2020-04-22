import datetime
from decimal import Decimal

from dateutil import parser

from coinuma_sdk.model import Model


class Trade(Model):
    _trade_id: int
    _price: Decimal
    _quote_volume: Decimal
    _base_volume: Decimal
    _timestamp: datetime.datetime
    _type: str

    def __init__(self, raw_data: dict) -> None:
        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'trade_id' in raw_data and raw_data['trade_id']:
            self.trade_id = raw_data['trade_id']
        if 'price' in raw_data and raw_data['price']:
            self.price = Decimal(raw_data['price'])
        if 'quote_volume' in raw_data and raw_data['quote_volume']:
            self.quote_volume = Decimal(raw_data['quote_volume'])
        if 'base_volume' in raw_data and raw_data['base_volume']:
            self.base_volume = Decimal(raw_data['base_volume'])
        if 'timestamp' in raw_data and raw_data['timestamp']:
            self.timestamp = parser.parse(raw_data['timestamp'])
        if 'type' in raw_data and raw_data['type']:
            self.type = raw_data['type']

    @property
    def trade_id(self) -> int:
        return self._trade_id
    
    @trade_id.setter
    def trade_id(self, value: int) -> None:
        assert isinstance(value, int)
        self._trade_id = value
    
    @property
    def price(self) -> Decimal:
        return self._price
    
    @price.setter
    def price(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._price = value
        
    @property
    def quote_volume(self) -> Decimal:
        return self._quote_volume
    
    @quote_volume.setter
    def quote_volume(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._quote_volume = value
        
    @property
    def base_volume(self) -> Decimal:
        return self._base_volume
    
    @base_volume.setter
    def base_volume(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._base_volume = value
    
    @property
    def timestamp(self) -> datetime.datetime:
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, value: datetime.datetime) -> None:
        assert isinstance(value, datetime.datetime)
        self._timestamp = value
        
    @property
    def type(self) -> str:
        return self._type
    
    @type.setter
    def type(self, value: str) -> None:
        assert isinstance(value, str)
        self._type = value
