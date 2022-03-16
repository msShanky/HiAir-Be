from pydantic import BaseModel
from datetime import datetime


class CandidateBase(BaseModel):
    candidate_id: int
    job_title: str
    date_of_application: str
    source_of_application: str
    candidate_name: str
    candidate_email: str
    candidate_phone: str
    current_location: str
    preffered_location: str
    total_experience: str
    current_company: str
    current_designation: str
