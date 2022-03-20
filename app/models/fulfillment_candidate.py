from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship
from app.db.session import Base


class FulfillmentCandidateScore(Base):
    __tablename__ = 'fulfillment_candidate_score'

    fulfillment_candidate_score_id = Column(
        Integer, primary_key=True, index=True)
    request_fulfillment_id = Column(Integer, ForeignKey(
        "request_fulfillment.request_fulfillment_id"))
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

    # request = relationship(
    #     "Request",
    #     back_populates="candidate_scrore"
    # )
    # candidate = relationship("Candidate", back_populates="candidate_scrore")
    # request_fulfillment = relationship(
    #     "RequestFulfillment",
    #     back_populates='candidate_scrore'
    # )

    class Config:
        orm_mode = True
