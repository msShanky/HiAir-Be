from pydantic import BaseModel


class CandidateScore(BaseModel):
    skill_set: float
    experience: float
    salary_range: float
    location: float
    industry: float
    domain: float
    notice_period: float


class CandidateBase(BaseModel):

    job_title: str
    date_of_application: str
    source_of_application: str
    candidate_name: str
    candidate_email: str
    candidate_phone: str
    current_location: str
    preffered_location: str
    current_salary: str
    total_experience: str
    current_company: str
    current_designation: str
    skill_set: str
    notice_period: str
    current_domain: str
    current_industry: str




class Candidate(CandidateBase):
    candidate_id: int


class CandidateWithScore(Candidate):
    hiair_score: str
    score_breakdown: CandidateScore