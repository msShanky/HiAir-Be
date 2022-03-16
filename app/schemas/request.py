from typing import List, Literal
from pydantic import BaseModel


class RequestBase(BaseModel):
    job_role: str
    salary_range: str
    job_location: List[str]
    turn_around_time: int
    domain: List[str]
    experience: str
    skill_set: List[str]
    notice_period: List[str]
    industry: List[str]
    no_of_profiles: int


class Request(RequestBase):
    request_id: int
