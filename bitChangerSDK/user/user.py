from .models import *
from bitChangerSDK.baseModule import BaseModule


class User(BaseModule):

	def balance(self, token: str) -> BalanceResponse:
		payload = {
			"token": token
		}
		response = self.send_request(payload, "POST", "/balance", BalanceResponse)
		return response

	def fetch(self) -> TokenFetchResponse:
		response = self.send_request({}, "POST", "/token/fetch", TokenFetchResponse)
		return response

	def fetch_commission(self, token: str) -> UserCommissionResponse:
		payload = {
			"token": token
		}
		response = self.send_request(payload, "POST", "/commission", UserCommissionResponse)
		return response

	def sign_up(self, invite_code: str) -> SignUpResponse:
		payload = {
			"invite_code": invite_code
		}
		response = self.send_request(payload, "POST", "/sign_up", SignUpResponse)
		return response
