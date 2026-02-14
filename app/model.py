from pydantic import BaseModel
from typing import List, Dict

class ExtractionResult(BaseModel):
    technical_skills: List[str]
    soft_skills: List[str]
    tools: List[str]
    experience_years: Dict[str, int]
    education: str
    certifications: List[str]

class MatchResponse(BaseModel):
    match_score: float
    embedding_similarity: float
    missing_skills: List[str]
    strengths: List[str]
    token_usage: dict
