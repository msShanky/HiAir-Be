from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base


class Request(Base):
    __tablename__ = 'request'

    request_id = Column(Integer, primary_key=True, index=True)
    request_status = Column(String)
    job_role = Column(String)
    salary_range = Column(String)
    job_location = Column(String)
    turn_around_time = Column(String)
    domain = Column(String)
    experience = Column(String)
    skill_set = Column(String)
    notice_period = Column(String)
    industry = Column(String)
    no_of_profiles = Column(String)

    # candidate_scrore = relationship(
    #     "FulfillmentCandidateScore",
    #     back_populates='request'
    # )
    # request_fulfillment = relationship(
    #     "RequestFulfillment", back_populates='request')

    class Config:
        orm_mode = True
