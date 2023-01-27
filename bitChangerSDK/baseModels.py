from pydantic import BaseModel

class KernelResponse(BaseModel):
	description: str
	status: str
