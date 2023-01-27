from pydantic import BaseModel

class CreatePayFormResponse(BaseModel):
	pay_form_url: str

class ExchangeRateResponse(BaseModel):
	exchange_rate: float
