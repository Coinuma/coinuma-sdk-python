import datetime
from decimal import Decimal

from coinuma_sdk.model import Model


class Order(Model):
    _orderID: int
    _userID: int
    _symbol: str
    _direction: str
    _order_type: str
    _status: str
    _price_limit: Decimal
    _price_stop: Decimal
    _price_average: Decimal
    _amount_initial: Decimal
    _amount_filled: Decimal
    _amount_pending: Decimal
    _commission: Decimal
    _date_created: datetime.datetime
    _date_active: datetime.datetime
    _date_completed: datetime.datetime
    _date_closed: datetime.datetime

    def __init__(self, raw_data: dict = None) -> None:
        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'orderID' in raw_data and raw_data['orderID']:
            self.orderID = raw_data['orderID']
        if 'userID' in raw_data and raw_data['userID']:
            self.userID = raw_data['userID']
        if 'symbol' in raw_data and raw_data['symbol']:
            self.symbol = raw_data['symbol']
        if 'direction' in raw_data and raw_data['direction']:
            self.direction = raw_data['direction']
        if 'order_type' in raw_data and raw_data['order_type']:
            self.order_type = raw_data['order_type']
        if 'status' in raw_data and raw_data['status']:
            self.status = raw_data['status']
        if 'price_limit' in raw_data and raw_data['price_limit']:
            self.price_limit = Decimal(raw_data['price_limit'])
        if 'price_stop' in raw_data and raw_data['price_stop']:
            self.price_stop = Decimal(raw_data['price_stop'])
        if 'price_average' in raw_data and raw_data['price_average']:
            self.price_average = Decimal(raw_data['price_average'])
        if 'amount_initial' in raw_data and raw_data['amount_initial']:
            self.amount_initial = Decimal(raw_data['amount_initial'])
        if 'amount_filled' in raw_data and raw_data['amount_filled']:
            self.amount_filled = Decimal(raw_data['amount_filled'])
        if 'amount_pending' in raw_data and raw_data['amount_pending']:
            self.amount_pending = Decimal(raw_data['amount_pending'])
        if 'commission' in raw_data and raw_data['commission']:
            self.commission = Decimal(raw_data['commission'])
        if 'date_created' in raw_data and raw_data['date_created']:
            self.date_created = raw_data['date_created']
        if 'date_active' in raw_data and raw_data['date_active']:
            self.date_active = raw_data['date_active']
        if 'date_completed' in raw_data and raw_data['date_completed']:
            self.date_completed = raw_data['date_completed']
        if 'date_closed' in raw_data and raw_data['date_closed']:
            self.date_closed = raw_data['date_closed']

    @property
    def orderID(self) -> int:
        return self._orderID

    @orderID.setter
    def orderID(self, value: int) -> None:
        assert isinstance(value, int)
        self._orderID = value

    @property
    def userID(self) -> int:
        return self._userID
    
    @userID.setter
    def userID(self, value: int) -> None:
        assert isinstance(value, int)
        self._userID = value
        
    @property
    def symbol(self) -> str:
        return self._symbol
    
    @symbol.setter
    def symbol(self, value: str) -> None:
        assert isinstance(value, str)
        self._symbol = value

    @property
    def direction(self) -> str:
        return self._direction

    @direction.setter
    def direction(self, value: str) -> None:
        assert isinstance(value, str)
        self._direction = value

    @property
    def order_type(self) -> str:
        return self._order_type

    @order_type.setter
    def order_type(self, value: str) -> None:
        assert isinstance(value, str)
        self._order_type = value

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        assert isinstance(value, str)
        self._status = value

    @property
    def price_limit(self) -> Decimal:
        return self._price_limit

    @price_limit.setter
    def price_limit(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._price_limit = Decimal(value)

    @property
    def price_stop(self) -> Decimal:
        return self._price_stop

    @price_stop.setter
    def price_stop(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._price_stop = Decimal(value)

    @property
    def price_average(self) -> Decimal:
        return self._price_average

    @price_average.setter
    def price_average(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._price_average = Decimal(value)

    @property
    def amount_initial(self) -> Decimal:
        return self._amount_initial

    @amount_initial.setter
    def amount_initial(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._amount_initial = Decimal(value)

    @property
    def amount_filled(self) -> Decimal:
        return self._amount_filled

    @amount_filled.setter
    def amount_filled(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._amount_filled = Decimal(value)

    @property
    def amount_pending(self) -> Decimal:
        return self._amount_pending

    @amount_pending.setter
    def amount_pending(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._amount_pending = Decimal(value)

    @property
    def commission(self) -> Decimal:
        return self._commission

    @commission.setter
    def commission(self, value: Decimal) -> None:
        assert isinstance(value, Decimal)
        self._commission = Decimal(value)

    @property
    def date_created(self) -> datetime.datetime:
        return self._date_created

    @date_created.setter
    def date_created(self, value: datetime.datetime):
        self._date_created = value

    @property
    def date_active(self) -> datetime.datetime:
        return self._date_active

    @date_active.setter
    def date_active(self, value: datetime.datetime):
        self._date_active = value

    @property
    def date_completed(self) -> datetime.datetime:
        return self._date_completed

    @date_completed.setter
    def date_completed(self, value: datetime.datetime):
        self._date_completed = value

    @property
    def date_closed(self) -> datetime.datetime:
        return self._date_closed

    @date_closed.setter
    def date_closed(self, value: datetime.datetime):
        self._date_closed = value
