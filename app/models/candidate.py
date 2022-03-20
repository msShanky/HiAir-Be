from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base


class Candidate(Base):
    __tablename__ = 'candidate'

    candidate_id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String)
    date_of_application = Column(String)
    source_of_application = Column(String)
    candidate_name = Column(String)
    candidate_email = Column(String)
    candidate_phone = Column(String)
    current_location = Column(String)
    preffered_location = Column(String)
    current_salary = Column(String)
    total_experience = Column(String)
    current_company = Column(String)
    current_designation = Column(String)
    skill_set = Column(String)
    notice_period = Column(String)
    current_domain = Column(String)
    current_industry = Column(String)

    # candidate_scrore = relationship(
    #     'FulfillmentCandidateScore',
    #     back_populates='candidate'
    # )

    class Config:
        orm_mode = True
