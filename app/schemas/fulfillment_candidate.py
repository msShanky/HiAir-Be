from pydantic import BaseModel


class FulfillmentCandidateBase(BaseModel):
    request_fulfillment_id: int
    request_id: int
    candidate_id: int
    hiair_score: float
    score_skill_set: float
    score_experience: float
    score_salary_range: float
    score_location: float
    score_industry: float
    score_domain: float
    score_notice_period: float


class FulfillmentCandidate(FulfillmentCandidateBase):
    fulfillment_candidate_score_id: int
