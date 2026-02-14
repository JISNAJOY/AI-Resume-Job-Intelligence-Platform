from fastapi import FastAPI, UploadFile, File, Form
from app.llm_service import extract_structured_data
from app.models import MatchResponse
from pathlib import Path

app = FastAPI(title="AI Resume Intelligence API")

prompt_path = Path("prompts/extraction_prompt.txt")
system_prompt = prompt_path.read_text()

@app.post("/analyze", response_model=MatchResponse)

#function analyzer with parameter resumeand job desc
async def analyze(
    resume: UploadFile = File(...), 
    job_description: str = Form(...)
):

 # LLM Extraction
    resume_data, usage1 = extract_structured_data(system_prompt, resume_text)
    job_data, usage2 = extract_structured_data(system_prompt, job_description)

 # Skill Matching
    resume_skills = combine_skills(resume_data)
    job_skills = combine_skills(job_data)

    match_score, missing, strengths = calculate_skill_match(
        resume_skills, job_skills
    )


