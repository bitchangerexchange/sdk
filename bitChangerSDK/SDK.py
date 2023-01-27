from .transaction import transaction
from .user import user
from .order import order
from .swap import swap

import hashlib
import hmac
import json
from typing import Dict


class SDKException(Exception):
	pass


class BaseSDK:

	def __init__(self, private_key: str, public_key: str):
		self.__private_key: str = private_key
		self.__public_key: str = public_key
		self._url: str = "https://exc.bit-changer.cc"

	def get_auth_headers(self, body: Dict = None) -> Dict:
		data = json.dumps(body) if body else self.__public_key
		signature = hmac.new(
			self.__private_key.encode("utf-8"),
			data.encode("utf-8"),
			hashlib.sha512,
		).hexdigest()

		return {
			"Content-Type": "application/json",
			"ApiPublic": self.__public_key,
			"Signature": signature
		}


class SDK(BaseSDK):

	def __init__(self, private_key: str, public_key: str):
		self.__base_sdk = super().__init__(private_key, public_key)

		self.Token = user.User(self._url, "/user", self)
		self.Transaction = transaction.Transaction(self._url, "/transaction", self)
		self.Order = order.Order(self._url, "/order", self)
		self.Swap = swap.Swap(self._url, "/swap", self)

	def set_auth_keys(self, private_key: str, public_key: str):
		self.__base_sdk = super().__init__(private_key, public_key)
