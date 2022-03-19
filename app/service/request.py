from sqlalchemy.orm import Session
from app.models.request import Request
from app.schemas.request import RequestBase

def get_all_request(db: Session):
    return db.query(Request).all()


def get_request_by_id(id: int, db: Session):
    return db.query(Request).filter(Request.request_id == id).first()


def create_request_handler(body: RequestBase, db: Session):
    db_body = Request(
        job_role=body.job_role,
        request_status="new",
        experience=body.experience,
        skill_set=','.join(body.skill_set),
        job_location=','.join(body.job_location),
        industry=','.join(body.industry),
        domain=','.join(body.domain),
        salary_range=body.salary_range,
        notice_period=','.join(body.notice_period),
        turn_around_time=str(body.turn_around_time),
        no_of_profiles=str(body.no_of_profiles)
    )
    db.add(db_body)
    db.commit()
    db.refresh(db_body)

    return db_body
