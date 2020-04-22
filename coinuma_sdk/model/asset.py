from decimal import Decimal

from coinuma_sdk.model import Model


class Asset(Model):
    _id: int
    _unified_cryptoasset_id: int
    _name: str
    _code: str
    _decimals: int
    _decimals_display: int
    _min_confirmations: int
    _min_deposit: Decimal
    _min_withdraw: Decimal
    _maker_fee: Decimal
    _taker_fee: Decimal
    _can_deposit: bool
    _can_withdraw: bool
    _active: bool

    def __init__(self, raw_data: dict) -> None:
        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'id' in raw_data and raw_data['id'] is not None:
            self.id = raw_data['id']
        if 'unified_cryptoasset_id' in raw_data:
            self.unified_cryptoasset_id = raw_data['unified_cryptoasset_id']
        if 'name' in raw_data and raw_data['name']:
            self.name = raw_data['name']
        if 'code' in raw_data and raw_data['code']:
            self.code = raw_data['code']
        if 'decimals' in raw_data and raw_data['decimals']:
            self.decimals = raw_data['decimals']
        if 'decimals_display' in raw_data and raw_data['decimals_display']:
            self.decimals_display = raw_data['decimals_display']
        if 'min_confirmations' in raw_data and raw_data['min_confirmations']:
            self.min_confirmations = raw_data['min_confirmations']
        if 'min_deposit' in raw_data and raw_data['min_deposit']:
            self.min_deposit = Decimal(raw_data['min_deposit'])
        if 'min_withdraw' in raw_data and raw_data['min_withdraw']:
            self.min_withdraw = Decimal(raw_data['min_withdraw'])
        if 'maker_fee' in raw_data and raw_data['maker_fee']:
            self.maker_fee = Decimal(raw_data['maker_fee'])
        if 'taker_fee' in raw_data and raw_data['taker_fee']:
            self.taker_fee = Decimal(raw_data['taker_fee'])
        if 'can_deposit' in raw_data and raw_data['can_deposit']:
            self.can_deposit = raw_data['can_deposit']
        if 'can_withdraw' in raw_data and raw_data['can_withdraw']:
            self.can_withdraw = raw_data['can_withdraw']
        if 'active' in raw_data:
            self.active = raw_data['active']

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        assert isinstance(value, int)
        self._id = value

    @property
    def unified_cryptoasset_id(self) -> int:
        return self._unified_cryptoasset_id

    @unified_cryptoasset_id.setter
    def unified_cryptoasset_id(self, value: int) -> None:
        assert isinstance(value, int)
        self._unified_cryptoasset_id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        assert isinstance(value, str)
        self._name = value

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, value: str) -> None:
        assert isinstance(value, str)
        self._code = value

    @property
    def decimals(self) -> int:
        return self._decimals

    @decimals.setter
    def decimals(self, value: int) -> None:
        assert isinstance(value, int)
        self._decimals = value

    @property
    def decimals_display(self) -> int:
        return self._decimals_display

    @decimals_display.setter
    def decimals_display(self, value: int) -> None:
        assert isinstance(value, int)
        self._decimals_display = value

    @property
    def min_confirmations(self) -> int:
        return self._min_confirmations

    @min_confirmations.setter
    def min_confirmations(self, value: int) -> None:
        assert isinstance(value, int)
        self._min_confirmations = value

    @property
    def min_deposit(self) -> Decimal:
        return self._min_deposit

    @min_deposit.setter
    def min_deposit(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._min_deposit = value

    @property
    def min_withdraw(self) -> Decimal:
        return self._min_withdraw

    @min_withdraw.setter
    def min_withdraw(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._min_withdraw = value

    @property
    def maker_fee(self) -> Decimal:
        return self._maker_fee

    @maker_fee.setter
    def maker_fee(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._maker_fee = value

    @property
    def taker_fee(self) -> Decimal:
        return self._taker_fee

    @taker_fee.setter
    def taker_fee(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._taker_fee = value

    @property
    def can_deposit(self) -> bool:
        return self._can_deposit

    @can_deposit.setter
    def can_deposit(self, value: bool) -> None:
        assert isinstance(value, bool)
        self._can_deposit = value

    @property
    def can_withdraw(self) -> bool:
        return self._can_withdraw

    @can_withdraw.setter
    def can_withdraw(self, value: bool) -> None:
        assert isinstance(value, bool)
        self._can_withdraw = value

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool) -> None:
        assert isinstance(value, bool)
        self._active = value
