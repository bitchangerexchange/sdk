import json
from typing import Dict, Any
import requests

from . import SDK


class ModuleException(Exception):
	pass

class BaseModule:

	def __init__(self, base_url: str, module_path: str, sdk: SDK.SDK):
		self.path = base_url + module_path
		self.sdk = sdk

	def send_request(self, payload: Dict, method: str, route: str, response_model: Any):
		resp = requests.request(method, url=f"{self.path}{route}", headers=self.sdk.get_auth_headers(payload),
		                        json=payload)
		if resp.status_code != 200:
			print(resp.text)
			raise ModuleException("connection refused")
		try:
			data = resp.json()
		except:
			raise ModuleException("error to parse json")
		try:
			response_data = response_model(**data)
		except Exception as e:
			raise ModuleException(e)
		return response_data