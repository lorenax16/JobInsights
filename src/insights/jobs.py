from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as csv_file:
      jobs = csv.DictReader(csv_file)
      jobs_list = []
      for job in jobs:
        jobs_list.append(job)
      return jobs_list
print(read("data/jobs.csv"))

def get_unique_job_types(path: str) -> List[str]:
   jobs = read(path)
   list_jobs = []
   for job in jobs:
    list_jobs.append(job["job_type"])
   return set(list_jobs)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    # """Filters a list of jobs by job_typ
    # Parameters
    # ----------
    # jobs : list
    #     List of jobs to be filtered
    # job_type : str
    #     Job type for the list filter

    # Returns
    # -------
    # list
    #     List of jobs with provided job_type
    # """
    # raise NotImplementedError

