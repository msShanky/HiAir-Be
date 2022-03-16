from sqlalchemy.orm import Session
from app.models import candidate


def get_all_candidates(db: Session):
    return db.query(candidate.Candidate).all()
