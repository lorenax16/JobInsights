from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salary_max = read(path)
    return max(
        [
            int(job["max_salary"])
            for job in salary_max
            if (job["max_salary"]).isdigit()
        ]
    )


def get_min_salary(path: str) -> int:
    salary_min = read(path)
    return min(
        [
            int(job["min_salary"])
            for job in salary_min
            if (job["min_salary"]).isdigit()
        ]
    )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if (type(job["min_salary"]) or type(job["max_salary"]) or salary) != int:
        raise ValueError
    if int(job["max_salary"]) < int(job["min_salary"]):
        raise ValueError
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    if matches_salary_range(jobs, salary):
        data = []
        data.append(jobs)
    return data
