from fastapi import FastAPI, UploadFile, File, Form
from app.llm_service import extract_structured_data
from app.embedding_service import get_embedding, cosine_similarity
from app.model import MatchResponse
from pathlib import Path
from app.utils import combine_skills
from app.matcher import calculate_skill_match

app = FastAPI(title="AI Resume Intelligence API")

prompt_path = Path("prompts/resume_prompt.txt")
system_prompt = prompt_path.read_text()

@app.post("/analyze", response_model=MatchResponse)

#function analyzer with parameter resumeand job desc
async def analyze(
    resume: UploadFile = File(...), 
    job_description: str = Form(...)
):
    resume_text = (await resume.read()).decode("utf-8")
    # LLM Extraction
    resume_data, usage1 = extract_structured_data(system_prompt, resume_text)
    job_data, usage2 = extract_structured_data(system_prompt, job_description)

    # Skill Matching
    resume_skills = combine_skills(resume_data)
    job_skills = combine_skills(job_data)

    match_score, missing, strengths = calculate_skill_match(
        resume_skills, job_skills
    )

     # Embedding Similarity
    resume_embedding = get_embedding(resume_text)
    job_embedding = get_embedding(job_description)

    similarity = cosine_similarity(resume_embedding, job_embedding)

    total_tokens = usage1.total_tokens + usage2.total_tokens

    return {
        "match_score": match_score,
        "embedding_similarity": round(similarity, 3),
        "missing_skills": missing,
        "strengths": strengths,
        "token_usage": {
            "total_tokens": total_tokens
        }
    }

