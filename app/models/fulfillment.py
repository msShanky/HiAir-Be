from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.session import Base


class RequestFulfillment(Base):
    __tablename__ = 'request_fulfillment'

    fulfillment_id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("request.request_id"))
    candidate_id = Column(Integer, ForeignKey("candidate.candidate_id"))
    hiair_score = Column(Float)
    score_skill_set = Column(Float)
    score_experience = Column(Float)
    score_salary_range = Column(Float)
    score_location = Column(Float)
    score_industry = Column(Float)
    score_domain = Column(Float)
    score_notice_period = Column(Float)

    request = relationship("Request", back_populates="request_fulfillment")
    candidate = relationship("Candidate", back_populates="request_fulfillment")

    class Config:
        orm_mode = True
