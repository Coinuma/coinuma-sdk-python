import base64
import hashlib
import hmac
import json
import time
from typing import Any

import requests

from coinuma_sdk.errors.connection import *


class Client:

    def __init__(self, base_url: str):
        self.base_url: str = base_url
        self._key_public: str = ''
        self._key_secret: str = ''
        self._hash_algorithm = hashlib.sha384

    def query(self, uri: str) -> Any:
        try:
            r = requests.get(self.base_url + uri)
        except requests.exceptions.ConnectionError:
            raise GeneralConnectionError('Connection error on endpoint: {}. Response: {}'.format(uri, r.text))
        return self.handle_response(r, uri)

    def query_authenticated(self, uri: str, method: str, payload: dict = None) -> Any:
        assert method in ('get', 'post', 'put', 'delete')

        if payload is None:
            payload = {}

        url = self.base_url + uri
        headers = self.build_headers(payload)

        requests_method = getattr(requests, method)
        try:
            r = requests_method(url, headers=headers, allow_redirects=False)
        except requests.exceptions.ConnectionError:
            raise GeneralConnectionError('Connection error on endpoint: {}'.format(uri))

        return self.handle_response(r, uri)

    def build_headers(self, payload: dict) -> dict:
        payload['timestamp'] = int(time.time()*1000)
        payload_b64 = base64.b64encode(json.dumps(payload).encode('utf-8'))
        signature = hmac.new(self.key_secret.encode('utf-8'), payload_b64, self._hash_algorithm).hexdigest()

        headers = {
            'Content-Type': "text/plain",
            'Content-Length': "0",
            'X-COINUMA-APIKEY': self.key_public,
            'X-COINUMA-PAYLOAD': payload_b64,
            'X-COINUMA-SIGNATURE': signature,
            'Cache-Control': "no-cache"
        }
        return headers

    @staticmethod
    def handle_response(r: requests.models.Response, uri: str) -> Any:
        if r.status_code == 200:
            return r.json()
        elif r.status_code == 400:
            raise BadRequestError('Bad request on endpoint: {}. Response: {}'.format(uri, r.text))
        elif r.status_code == 404:
            raise EndpointNotExistsError('The endpoint does not exist: {}. Response: {}'.format(uri, r.text))
        elif r.status_code == 429:
            raise TooManyRequestsError('Too many requests on endpoint: {}. Response: {}'.format(uri, r.text))
        elif r.status_code == 500:
            raise InternalServerError('Internal server error on endpoint: {}. Response: {}'.format(uri, r.text))
        else:
            raise GeneralConnectionError('Connection error on endpoint: {}. Response: {}'.format(uri, r.text))

    @property
    def key_public(self) -> str:
        return self._key_public

    @key_public.setter
    def key_public(self, value: str) -> None:
        assert isinstance(value, str)
        self._key_public = value

    @property
    def key_secret(self) -> str:
        return self._key_secret

    @key_secret.setter
    def key_secret(self, value: str) -> None:
        assert isinstance(value, str)
        self._key_secret = value
