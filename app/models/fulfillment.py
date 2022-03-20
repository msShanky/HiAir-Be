from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship
from app.db.session import Base


class RequestFulfillment(Base):
    __tablename__ = 'request_fulfillment'

    request_fulfillment_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String)
    request_id = Column(Integer, ForeignKey("request.request_id"))

    # request = relationship("Request", back_populates="request_fulfillment")    
    # candidate_scrore = relationship(
    #     "FulfillmentCandidateScore",
    #     back_populates='request_fulfillment'
    # )

    class Config:
        orm_mode = True
