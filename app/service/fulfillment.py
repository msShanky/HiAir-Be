from sqlalchemy.orm import Session
from app.models.candidate import Candidate
from app.models.fulfillment import RequestFulfillment
from app.models.request import Request
from app.models.fulfillment_candidate import FulfillmentCandidateScore
from app.schemas.candidate import CandidateWithScore
from uuid import uuid4
from devtools import debug


def get_fulfillment_by_id(id: int, db: Session):
    return db.query(RequestFulfillment).filter(RequestFulfillment.request_id == id).first()

# TODO: Create a new function to add records to the DB for candidate_score


def create_request_fulfillment(db: Session, db_request_fulfillment: RequestFulfillment) -> RequestFulfillment:
    try:
        db_fulfillment = db_request_fulfillment
        db.add(db_fulfillment)
        db.commit()
        created_fulfillment: RequestFulfillment = db.query(RequestFulfillment).filter(
            RequestFulfillment.request_id == db_request_fulfillment.request_id
        ).first()
        print("DB Response", db_fulfillment)
        return created_fulfillment
    except Exception as exception:
        debug(exception, 'The exception is')


def create_fulfillment_request(candidates: list[CandidateWithScore], request: Request, db: Session):
    session_id = uuid4()
    print(" ---- CREATING NEW FULFILLMENT ---- ")
    db_request_fulfillment = RequestFulfillment(
        session_id=session_id,
        request_id=request.request_id
    )
    response = create_request_fulfillment(db, db_request_fulfillment)
    debug(response, "((((( RESPONSE )))))))")

    fulfillment_data = []
    for candidate in candidates:
        fulfillment_candidate_data = FulfillmentCandidateScore(
            hiair_score=candidate.hiair_score,
            request_fulfillment_id=response.request_fulfillment_id,
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

    print("AFTER ADDING CANDIDATE RECORDS +++++")

    # debug(fulfillment_data)
    # debug(response)
    db.commit()
    return response
