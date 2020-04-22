from decimal import Decimal

from coinuma_sdk.model import Model
from coinuma_sdk.model.asset import Asset


class Symbol(Model):
    _code: str
    _asset_base: Asset
    _asset_quote: Asset
    _tick_size: Decimal
    _minimum_order_size: Decimal
    _active: bool

    def __init__(self, raw_data: dict = None) -> None:
        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'code' in raw_data and raw_data['code']:
            self.code = raw_data['code']
        if 'asset_base' in raw_data and raw_data['asset_base']:
            self.asset_base = Asset(raw_data['asset_base'])
        if 'asset_quote' in raw_data and raw_data['asset_quote']:
            self.asset_quote = Asset(raw_data['asset_quote'])
        if 'tick_size' in raw_data and raw_data['tick_size']:
            self.tick_size = Decimal(raw_data['tick_size'])
        if 'minimum_order_size' in raw_data and raw_data['minimum_order_size']:
            self.minimum_order_size = Decimal(raw_data['minimum_order_size'])
        if 'active' in raw_data:
            self.active = raw_data['active']
            
    @property
    def code(self) -> str:
        return self._code
    
    @code.setter
    def code(self, value: str) -> None:
        assert isinstance(value, str)
        self._code = value
        
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
    def tick_size(self) -> Decimal:
        return self._tick_size
    
    @tick_size.setter
    def tick_size(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._tick_size = value
        
    @property
    def minimum_order_size(self) -> Decimal:
        return self._minimum_order_size
    
    @minimum_order_size.setter
    def minimum_order_size(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._minimum_order_size = value
        
    @property
    def active(self) -> bool:
        return self._active
    
    @active.setter
    def active(self, value: bool) -> None:
        assert isinstance(value, bool)
        self._active = value
