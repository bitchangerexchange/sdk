from pydantic import BaseModel

class CreatePayFormResponse(BaseModel):
	pay_form_link: str

class ExchangeRateResponse(BaseModel):
	exchange_rate: float
