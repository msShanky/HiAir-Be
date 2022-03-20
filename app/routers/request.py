
from copy import deepcopy
from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_db
from fastapi.encoders import jsonable_encoder
# from app.models.candidate import Candidate
from app.schemas.candidate import CandidateWithScore
from app.models.request import Request
from app.schemas.fulfillment import RequestFulfillmentBase
from app.models.fulfillment import RequestFulfillment
from app.schemas.request import RequestBase
from app.service.candidate import get_all_candidates, get_candidate_by_id
from app.service.fulfillment import create_fulfillment_request, get_fulfillment_by_id
from app.service.request import create_request_handler,  get_all_request, get_request_by_id
from app.service.matchmaking import domain_matching, experience_matching, industry_matching, location_matching, notice_period_matching, salary_range_matching, skill_set_matching
from sqlalchemy.orm import Session
import pandas as pd
from devtools import debug


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
    try:
        fulfillment_for_id: RequestFulfillment | None = get_fulfillment_by_id(
            request_id, db
        )
        print(fulfillment_for_id, "fulfillment_for_id")
        debug(fulfillment_for_id)
    except Exception as e:
        print("There is an error with fetching fulfillment -----------------", e)
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    candidates: list[CandidateWithScore] = get_all_candidates(db)
    request: Request = get_request_by_id(request_id, db)
    if request == None:
        raise HTTPException(
            status_code=404,
            detail="Cannot find the request information for the provided id"
        )

    # try:
    for candidate in candidates:
        candidate_score: CandidateScore = {
            "skill_set": skill_set_matching(
                request.skill_set,
                candidate
            ),
            "experience": experience_matching(
                request.experience,
                candidate
            ),
            "salary_range": salary_range_matching(
                request.salary_range,
                candidate
            ),
            "location": location_matching(
                request.job_location,
                candidate
            ),
            "industry": industry_matching(
                request.industry,
                candidate
            ),
            "domain": domain_matching(
                request.domain,
                candidate
            ),
            "notice_period": notice_period_matching(
                request.notice_period,
                candidate
            )
        }

        candidate_hiair_score = round(sum(candidate_score.values())/7, 2)
        candidate.hiair_score = candidate_hiair_score
        candidate.score_breakdown = candidate_score

    sorted_candidates: list[CandidateWithScore] = sorted(
        candidates,
        key=lambda k: k.hiair_score,
        reverse=True
    )
    old_sorted_list = deepcopy(sorted_candidates)
    print("THE NONE CONDITION", fulfillment_for_id == None)
    # except Exception as e:
    # 		debug("Exception when calculating score", e)

    try:
        if fulfillment_for_id == None:
            create_fulfillment_request(sorted_candidates, request, db)
        # debug("Total Profiles", int(request.no_of_profiles))
        # debug(old_sorted_list)
        # response = deepcopy(sorted_candidates)
        # print(response[0].__dict__)
        return old_sorted_list[0:int(request.no_of_profiles)]
    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Error when creating fulfillment request" + str(exception))


@ router.post('/')
async def create_request(request: RequestBase, db: Session = Depends(get_db)):
    db_values = create_request_handler(request, db)

    return db_values
