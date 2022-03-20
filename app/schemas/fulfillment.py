from pydantic import BaseModel


class RequestFulfillmentBase(BaseModel):
    request_id: int
    session_id: str


class RequestFulfillment(RequestFulfillmentBase):
    request_fulfillment_id: int
