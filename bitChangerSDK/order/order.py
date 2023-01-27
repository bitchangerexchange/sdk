from .models import *
from bitChangerSDK.baseModule import BaseModule


class Order(BaseModule):

	def create_pay_form(self, token: str, amount: float, callback_url: str) -> CreatePayFormResponse:
		payload = {
			"token": token,
			"amount": amount,
			"callback_url": callback_url,
		}
		response = self.send_request(payload, "POST", "/pay_form/create", CreatePayFormResponse)
		return response

	def get_exchange_rate(self, token_from: str, token_to: str) -> ExchangeRateResponse:
		payload = {
			"token_from": token_from,
			"token_to": token_to
		}
		response = self.send_request(payload, "POST", "/exchange_rate", ExchangeRateResponse)
		return response
