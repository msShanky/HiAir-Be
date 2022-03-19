from pydantic import BaseModel


class RequestFulfillmentBase(BaseModel):
    request_id: int
    session_id: str
    candidate_id: int
    hiair_score: float
    score_skill_set: float
    score_experience: float
    score_salary_range: float
    score_location: float
    score_industry: float
    score_domain: float
    score_notice_period: float


class RequestFulfillment(RequestFulfillmentBase):
    fulfillment_id: int
