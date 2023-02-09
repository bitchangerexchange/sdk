from datetime import datetime
from typing import List

from pydantic import BaseModel


class TransactionCreateInResponse(BaseModel):
	description: str = None
	dest_tag: str = None
	address: str
	alter_refer: str = None
	status: str = None
	currency_name: str
	external_id: str


class TransactionCreateOutResponse(BaseModel):
	description: str
	status: str
	external_id: str


class TransactionGetResponse(BaseModel):
	amount: float
	callback_url: str
	date_create: datetime
	dest_tag: str
	hash: str
	receiver: str
	success: bool
	done: bool
	error: bool
	token: str
	external_id: str
	fee: float
	type: str
	done_time: datetime


class TransactionFetchResponse(BaseModel):
	transactions: List[TransactionGetResponse]
