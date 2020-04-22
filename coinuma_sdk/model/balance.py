from decimal import Decimal

from coinuma_sdk.model import Model


class Balance(Model):
    _code: str
    _name: str
    _type: str
    _balance: Decimal
    _balance_orders: Decimal
    _active: bool

    def __init__(self, raw_data: dict = None) -> None:
        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'code' in raw_data and raw_data['code']:
            self.code = raw_data['code']
        if 'name' in raw_data and raw_data['name']:
            self.name = raw_data['name']
        if 'type' in raw_data and raw_data['type']:
            self.type = raw_data['type']
        if 'balance' in raw_data and raw_data['balance']:
            self.balance = Decimal(raw_data['balance'])
        if 'balance_orders' in raw_data and raw_data['balance_orders']:
            self.balance_orders = Decimal(raw_data['balance_orders'])
        if 'active' in raw_data and raw_data['active']:
            self.active = raw_data['active']

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, value: str) -> None:
        assert isinstance(value, str)
        self._code = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        assert isinstance(value, str)
        self._name = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        assert isinstance(value, str)
        self._type = value

    @property
    def balance(self) -> Decimal:
        return self._balance

    @balance.setter
    def balance(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._balance = value

    @property
    def balance_orders(self) -> Decimal:
        return self._balance_orders

    @balance_orders.setter
    def balance_orders(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._balance_orders = value

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool) -> None:
        assert isinstance(value, bool)
        self._active = value
