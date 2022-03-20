from http.client import HTTPException
from sqlalchemy.orm import Session
from app.models.candidate import Candidate


def get_all_candidates(db: Session):
    try:
        db_candidates = db.query(Candidate).all()        
        return db_candidates
    except:
        print("There is an error from fetching candidates")
        raise HTTPException(
            status_code=404,
            detail="Cannot fetch information from DB for candidates"
        )


def get_candidate_by_id(id: int, db: Session):
    return db.query(Candidate).filter(Candidate.candidate_id == id).first()
