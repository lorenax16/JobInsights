from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries = read(path)
    industries_list = []
    for industry in industries:
        industries_list.append(industry['industry'])
    return set(industries_list)

def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job['industry'] == industry]
