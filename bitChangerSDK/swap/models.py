from pydantic import BaseModel
from datetime import datetime


class SwapGetResponse(BaseModel):
	create_time: datetime
	execute_time: datetime
	status: str
	currency_from: str
	currency_to: str
	rate: float
	external_id: str
	amount_from: float
	amount_to: float
	callback_url: str
	pay_form_url: str


class SwapCreateResponse(BaseModel):
	exc_rate: float
	amount_to: float
	external_id: str
