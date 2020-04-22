import datetime
from decimal import Decimal
from typing import List

from coinuma_sdk.api.client import Client
from coinuma_sdk.const import endpoints_private, url_addresses
from coinuma_sdk.model.order import Order
from coinuma_sdk.model.balance import Balance


class Private:

    def __init__(self, key_public: str, key_secret: str) -> None:
        self._client: Client = Client(url_addresses.PRIVATE)
        self._client.key_public = key_public
        self._client.key_secret = key_secret

    def get_order(self, order_id: int) -> Order:
        response = self._client.query_authenticated(endpoints_private.ORDER.format(orderID=order_id), 'get')
        return Order(response['data'])

    def get_orders(
            self,
            symbol: str = None,
            page: int = None,
            limit: int = None,
            status: str = None,
            date_start: datetime.datetime = None,
            date_end: datetime.datetime = None
    ) -> List[Order]:
        raw_payload = {
            'symbol': symbol,
            'page': page,
            'limit': limit,
            'status': status,
            'date_start': date_start,
            'date_end': date_end
        }
        payload = {k: v for k, v in raw_payload.items() if v is not None}

        response = self._client.query_authenticated(endpoints_private.ORDERS, 'get', payload=payload)
        return [Order(raw_element) for raw_element in response['data']['data']]

    def new_order(
            self,
            symbol: str,
            direction: str,
            order_type: str,
            amount: Decimal,
            price_limit: Decimal = None,
            price_stop: Decimal = None
    ) -> bool:
        payload = {
            'symbol': symbol,
            'amount': '{0:f}'.format(amount),
            'direction': direction,
            'order_type': order_type
        }
        if price_limit:
            payload['price_limit'] = '{0:f}'.format(price_limit)
        if price_stop:
            payload['price_stop'] = '{0:f}'.format(price_stop)
        response = self._client.query_authenticated(endpoints_private.ORDER_NEW, 'post', payload)

        return True if response['status'] == 'success' else False

    def cancel_order(self, orderID: int) -> bool:
        payload = {
            'orderID': orderID
        }
        response = self._client.query_authenticated(endpoints_private.ORDER_CANCEL, 'put', payload)
        return True if response['status'] == 'success' else False

    def cancel_all_orders(self) -> bool:
        response = self._client.query_authenticated(endpoints_private.ORDER_CANCEL_ALL, 'put')
        return True if response['status'] == 'success' else False

    def get_balance(self, display_zero_balances: bool = True) -> List[Balance]:
        payload = {
            'display_zero_balances': display_zero_balances
        }
        response = self._client.query_authenticated(endpoints_private.ACCOUNT_BALANCE, 'get', payload)
        return [Balance(raw_element) for raw_element in response['data']]

    def get_transactions(
            self,
            page: int = None,
            limit: int = None,
            symbol: str = None,
            currencies: list = None,
            transaction_type: str = None,
            date_start: datetime.datetime = None,
            date_end: datetime.datetime = None
    ):
        raw_payload = {
            'page': page,
            'limit': limit,
            'symbol': symbol,
            'currencies': currencies,
            'type': transaction_type,
            'date_start': date_start,
            'date_end': date_end
        }

        payload = {k: v for k, v in raw_payload.items() if v is not None}

        response = self._client.query_authenticated(endpoints_private.ACCOUNT_TRANSACTIONS, 'get', payload)
        return response

