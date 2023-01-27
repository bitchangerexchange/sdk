from .models import *
from bitChangerSDK.baseModule import BaseModule


class Transaction(BaseModule):

	def transaction_create_in(self, token: str, callback_url: str, card_number: str, amount: float, email: str) -> TransactionCreateInResponse:
		payload = {
			"token": token,
			"callback_url": callback_url,
			"card_number": card_number,
			"amount": amount,
			"email": email
		}
		response = self.send_request(payload, "POST", "/create/in", TransactionCreateInResponse)
		return response

	def transaction_create_out(self, token: str, receiver: str, amount: float, callback_url: str) -> TransactionCreateOutResponse:
		payload = {
			"token": token,
			"receiver": receiver,
			"amount": amount,
			"callback_url": callback_url,
		}
		response = self.send_request(payload, "POST", "/create/out", TransactionCreateOutResponse)
		return response

	def transaction_get(self, external_id: str, transaction_type: str) -> TransactionGetResponse:
		payload = {
			"external_id": external_id,
			"type": transaction_type
		}
		response = self.send_request(payload, "POST", "/get", TransactionGetResponse)
		return response

	def transaction_fetch(self, limit: int, offset: int, sort_order: str) -> TransactionFetchResponse:
		payload = {
			"limit": limit,
			"offset": offset,
			"sort_order": sort_order
		}
		response = self.send_request(payload, "POST", "/fetch", TransactionFetchResponse)
		return response
