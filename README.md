# 🤖 LLM Resume Analyzer API

An AI-powered FastAPI backend that analyzes resumes against job descriptions and calculates a structured match score using LLM-based skill extraction and semantic similarity.

Built to demonstrate clean backend architecture, AI integration, and scalable API design.

---

## 🚀 Features

- Extracts structured skills from resumes using LLM
- Compares resume against job description
- Calculates:
  - Skill match score
  - Missing skills
  - Strength areas
  - Embedding-based semantic similarity
- Token usage tracking
- Mock mode for development without API cost
- Interactive API documentation via Swagger

---

## 🏗️ Architecture

The project follows a clean service-layer structure:

- **API Layer** – FastAPI routes  
- **LLM Service** – Structured data extraction  
- **Embedding Service** – Semantic similarity calculation  
- **Matching Engine** – Scoring logic  
- **Config Layer** – Environment-based configuration  

Designed to allow easy switching between Mock mode and real LLM integration.

---

## 🛠️ Tech Stack

**Backend:**  
Python, FastAPI, Pydantic

**AI & NLP:**  
OpenAI API, Embeddings, Cosine Similarity

**DevOps:**  
Docker, Uvicorn, Environment Variables (.env)

---

## 📊 Example Response

```json
{
  "match_score": 82,
  "embedding_similarity": 0.91,
  "missing_skills": ["Kubernetes", "AWS"],
  "strengths": ["Python", "FastAPI", "Docker"],
  "token_usage": {
    "total_tokens": 420
  }
}