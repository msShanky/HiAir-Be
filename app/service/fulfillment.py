from sqlalchemy.orm import Session
from app.models.candidate import Candidate
from app.models.request import Request
from app.models.fulfillment import RequestFulfillment
from app.schemas.candidate import CandidateWithScore
from uuid import uuid4
# from app.schemas.fulfillment import RequestFulfillmentBase


def create_feedback_fulfillment(candidates: list[CandidateWithScore], request: Request, db: Session):

    fulfillment_data = []
    session_id = uuid4()
    for candidate in candidates:
        fulfillment_candidate_data = RequestFulfillment(
            hiair_score=candidate.hiair_score,
            session_id=session_id,
            request_id=request.request_id,
            candidate_id=candidate.candidate_id,
            score_skill_set=candidate.score_breakdown['skill_set'],
            score_experience=candidate.score_breakdown['experience'],
            score_salary_range=candidate.score_breakdown['salary_range'],
            score_location=candidate.score_breakdown['location'],
            score_domain=candidate.score_breakdown['domain'],
            score_industry=candidate.score_breakdown['industry'],
            score_notice_period=candidate.score_breakdown['notice_period']
        )
        fulfillment_data.append(fulfillment_candidate_data)

    response = db.add_all(fulfillment_data)
    db.commit()
    return response
