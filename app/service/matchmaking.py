# Used for assigning points to the skill matches
from app.schemas.candidate import Candidate

# local_skills = 'SQL,Oracle,HTML,NODE'


def range_points_calculator(compare_value: int, rangeArray: list[str]) -> float:
    # print("THE compare value received is", compare_value)
    # print("The range array received for points", rangeArray)
    start_range, end_range = rangeArray
    max_start_range = int(start_range) - 1
    buffer_end_range = int(end_range) + 1
    max_end_range = int(end_range) + 3
    # print("RANGE START", start_range, "RANGE END", end_range)
    # print("MAX START RANGE", max_start_range)
    # print("BUFFER END RANGE", buffer_end_range)
    # print("MAX END RANGE", max_end_range)

    # IF CLOSE TO max_start_range .25
    # IF EXACT between start_range and end_range 1 => Done
    # IF CLOSE TO buffer_end_range but less than max_end_range .5
    # IF OVER THE max_end_range then 0

    if compare_value >= int(start_range) and compare_value <= int(end_range):
        # The candidate gets 1 point
        return 1
    elif compare_value >= int(buffer_end_range) and compare_value <= max_end_range:
        # The candidate gets .5 points
        return .5
    elif compare_value >= max_start_range and compare_value <= int(start_range):
        # The candidate gets .25 point
        return .25
    elif compare_value > max_end_range:
        # The candidate gets 0 point
        return 0

    return 0


def point_matching_calculator(items_to_match: str, candidate_info: str) -> float:
    matching_points = 0
    items_to_match_lower = items_to_match.lower()
    candidate_info_lower = candidate_info.lower()
    point_for_match = round(1/len(items_to_match_lower.split(',')), 2)
    candidate_info_list = candidate_info_lower.split(',')
    items_to_match_list = items_to_match_lower.split(',')
    for item in items_to_match_list:
        if item in candidate_info_list:
            matching_points = matching_points + point_for_match

    return round(matching_points, 2)


def skill_set_matching(skills_to_match: str, candidate) -> float:
    # candidate_skills_value = candidate.skill_set
    # if skills_to_match != None:
    #     skill_list = skills_to_match.split(',')
    # else:
    #     skill_list = ['']

    # skill_point = round(1/len(skill_list), 2)
    # points = 0

    # if candidate_skills_value is not None:
    #     candidate_skill_list = candidate_skills_value.split(',')
    #     for skill in skill_list:
    #         if skill in candidate_skill_list:
    #             points = skill_point + points
    points = point_matching_calculator(skills_to_match, candidate.skill_set)
    # print("Points for Skills => ", round(points, 2))
    return round(points, 2)


def experience_matching(experience: str, candidate: Candidate) -> float:
    candidate_experience_value = candidate.total_experience    
    candidate_experience = float(candidate_experience_value)
    points = range_points_calculator(
        candidate_experience,
        experience.split('_')
    )
    # print("Received input", experience)
    # print("Candidate experience", candidate_experience)
    # print("Points for Experience => ", points)
    # max_start_range = int(start_range) - 1
    # buffer_end_range = int(end_range) + 1
    # max_end_range = int(end_range) + 3
    # # print("RANGE START", start_range, "RANGE END", end_range)
    # # print("MAX START RANGE", max_start_range)
    # # print("BUFFER END RANGE", buffer_end_range)
    # # print("MAX END RANGE", max_end_range)

    # # IF CLOSE TO max_start_range .25
    # # IF EXACT between start_range and end_range 1 => Done
    # # IF CLOSE TO buffer_end_range but less than max_end_range .5
    # # IF OVER THE max_end_range then 0

    # if candidate_experience >= int(start_range) and candidate_experience <= int(end_range):
    #     # The candidate gets 1 point
    #     return 1
    # elif candidate_experience >= int(buffer_end_range) and candidate_experience <= max_end_range:
    #     # The candidate gets .5 points
    #     return .5
    # elif candidate_experience >= max_start_range and candidate_experience <= int(start_range):
    #     # The candidate gets .25 point
    #     return .25
    # elif candidate_experience > max_end_range:
    #     # The candidate gets 0 point
    #     return 0

    # else:
    # The candidate gets .25 point
    # return 0
    return points


def salary_range_matching(salary_range: str, candidate: Candidate) -> float:
    points = range_points_calculator(
        float(candidate.current_salary),
        salary_range.split('-')
    )
    # candidate_salary = int(candidate.current_salary)
    # _, end_range = salary_range.split('-')
    # max_end_range = int(end_range) + 2
    # if candidate_salary <= int(end_range):
    #     points = 1
    # elif candidate_salary > int(end_range) and candidate_salary <= max_end_range:
    #     points = .5
    # elif candidate_salary > max_end_range:
    #     points = 0

    return points


def location_matching(requested_locations: str, candidate: Candidate) -> float:
    points = point_matching_calculator(
        requested_locations,
        candidate.preffered_location
    )
    # print("Points for location matching =>", points)
    return points


def industry_matching(requested_industry: str, candidate: Candidate) -> float:
    points = point_matching_calculator(
        requested_industry,
        candidate.current_industry
    )
    # print("Points for industry =>", points)
    return points


def domain_matching(requested_domain: str, candidate: Candidate) -> float:
    points = point_matching_calculator(
        requested_domain,
        candidate.current_domain
    )
    # print("Points for industry =>", points)
    return points


def notice_period_matching(requested_notice_period: str, candidate: Candidate) -> float:
    points = range_points_calculator(
        int(candidate.notice_period),
        requested_notice_period.split(',')
    )
    # print("The points generated for notice period is", points)
    return points
