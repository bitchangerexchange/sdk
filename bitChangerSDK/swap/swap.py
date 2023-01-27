from .models import *
from bitChangerSDK.baseModule import BaseModule


class Swap(BaseModule):

	def swap_create(self, token_from: str, amount: float, callback_url: str) -> SwapCreateResponse:
		payload = {
			"token_from": token_from,
			"amount": amount,
			"callback_url": callback_url,
		}
		response = self.send_request(payload, "POST", "/create", SwapCreateResponse)
		return response

	def swap_get(self, external_id: str) -> SwapGetResponse:
		payload = {
			"external_id": str
		}
		response = self.send_request(payload, "POST", f"/{external_id}/get", SwapGetResponse)
		return response
