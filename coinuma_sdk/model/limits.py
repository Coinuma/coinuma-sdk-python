from coinuma_sdk.model import Model


class Limits(Model):
    _requests: int
    _orders: int

    def __init__(self, raw_data: dict = None) -> None:
        if raw_data:
            self.map_raw_data(raw_data)

    def map_raw_data(self, raw_data: dict) -> None:
        if 'requests' in raw_data and raw_data['requests']:
            self.requests = raw_data['requests']
        if 'orders' in raw_data and raw_data['orders']:
            self.orders = raw_data['orders']

    @property
    def requests(self) -> int:
        return self._requests

    @requests.setter
    def requests(self, value: int) -> None:
        assert isinstance(value, int)
        self._requests = value

    @property
    def orders(self) -> int:
        return self._orders

    @orders.setter
    def orders(self, value: int) -> None:
        assert isinstance(value, int)
        self._orders = value

