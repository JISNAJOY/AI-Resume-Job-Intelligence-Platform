def calculate_skill_match(resume_skills, job_skills):
    resume_set = set([s.lower() for s in resume_skills])
    job_set = set([s.lower() for s in job_skills])

    matched = resume_set.intersection(job_set)
    missing = job_set - resume_set

    if len(job_set) == 0:
        score = 0
    else:
        score = (len(matched) / len(job_set)) * 100

    return round(score, 2), list(missing), list(matched)
