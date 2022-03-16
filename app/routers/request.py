from fastapi import APIRouter, Depends
from sqlalchemy import JSON
from app.dependencies import get_db
from app.models.request import Request
from app.schemas.request import RequestBase
from app.service.candidate import get_all_candidates
from app.service.request import create_request_handler, domain_matching, experience_matching, get_all_request, get_request_by_id, industry_matching, location_matching, notice_period_matching, salary_range_matching, skill_set_matching
from sqlalchemy.orm import Session
import pandas as pd


class CandidateScore:
    skill_set: int
    experience: int
    salary_range: int
    location: int
    industry: int
    domain: int
    notice_period: int

# candidate_score = {
#     "skill_set": 0,
#     "experience": 0,
#     "salary_range": 0,
#     "location": 0,
#     "industry": 0,
#     "domain": 0,
#     "notice_period": 0
# }


router = APIRouter(
    prefix='/request',
    tags=['request'],
    dependencies=[],
    responses={404: {"description": "Not found"}}
)


@router.get('/')
async def read_users(db: Session = Depends(get_db)):
    return get_all_request(db)


@router.get('/result/{request_id}')
async def read_users(request_id: int, db: Session = Depends(get_db)):
    candidates = get_all_candidates(db)
    request: Request = get_request_by_id(request_id, db)

    for candidate in candidates:
        candidate_score = CandidateScore()
        candidate_score.skill_set = skill_set_matching(
            request.skill_set,
            candidate
        )
        candidate_score.experience = experience_matching()
        candidate_score.salary_range = salary_range_matching()
        candidate_score.location = location_matching()
        candidate_score.industry = industry_matching()
        candidate_score.domain = domain_matching()
        candidate_score.notice_period = notice_period_matching()

        candidate_score_list = candidate_score.__dict__
        for key in candidate_score_list:
            print("INDIVIDUAL SCORE FOR ", key,
                  " IS =>  ", candidate_score_list[key])

        print("CANDIDATE SCORE", candidate_score_list)
    return candidates


@router.post('/')
async def create_request(request: RequestBase, db: Session = Depends(get_db)):
    db_values = create_request_handler(request, db)

    return db_values
