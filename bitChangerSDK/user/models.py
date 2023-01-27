from typing import List

from pydantic import BaseModel


class UserCommissionResponse(BaseModel):
	token: str
	sum_comm_in: float
	sum_comm_out: float
	fix_comm_in: float
	fix_comm_out: float
	min_deposit_sum: float
	min_withdrawal_sum: float


class SignUpResponse(BaseModel):
	public_key: str
	private_key: str


class BalanceResponse(BaseModel):
	balance: float


class TokenFetchResponse(BaseModel):
	tokens: List[str]
