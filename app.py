import os
import json
import re
import tempfile
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import PyPDF2
import io
from typing import List
import uvicorn

app = FastAPI(title="AI Resume Screener", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Gemini
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from PDF bytes using PyPDF2."""
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"Error extracting PDF: {str(e)}"

def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    """Extract text based on file type."""
    if filename.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_bytes)
    elif filename.lower().endswith('.txt'):
        return file_bytes.decode('utf-8', errors='ignore')
    else:
        # Try as text
        try:
            return file_bytes.decode('utf-8', errors='ignore')
        except:
            return "Unable to extract text from file."

def analyze_resumes_with_gemini(jd_text: str, resumes: list[dict]) -> dict:
    """Send JD + resumes to Gemini for analysis."""
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY not configured")
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    resumes_text = ""
    for i, resume in enumerate(resumes):
        resumes_text += f"\n\n--- RESUME {i+1}: {resume['name']} ---\n{resume['text']}"
    
    prompt = f"""You are an expert HR AI assistant and talent acquisition specialist.

Analyze the following Job Description and {len(resumes)} resumes. Rank candidates from best to worst fit.

=== JOB DESCRIPTION ===
{jd_text}

=== RESUMES ===
{resumes_text}

Return a JSON object ONLY (no markdown, no explanation) with this exact structure:
{{
  "ranked_candidates": [
    {{
      "rank": 1,
      "name": "candidate name or Resume 1 if name not found",
      "filename": "filename",
      "overall_score": 92,
      "match_percentage": 92,
      "verdict": "Strong Match" | "Good Match" | "Partial Match" | "Weak Match",
      "verdict_color": "green" | "blue" | "yellow" | "red",
      "skills_matched": ["skill1", "skill2"],
      "skills_missing": ["skill1", "skill2"],
      "experience_score": 85,
      "skills_score": 90,
      "education_score": 80,
      "culture_score": 75,
      "strengths": ["strength 1", "strength 2", "strength 3"],
      "weaknesses": ["weakness 1", "weakness 2"],
      "hiring_recommendation": "Detailed 2-3 sentence recommendation about whether to hire this candidate and why.",
      "interview_questions": ["Question 1?", "Question 2?", "Question 3?"]
    }}
  ],
  "summary": {{
    "total_candidates": {len(resumes)},
    "top_recommendation": "Name of best candidate",
    "analysis_insight": "2-3 sentence overall insight about the candidate pool"
  }}
}}

Be precise, fair, and detailed. Score out of 100 for each category."""

    response = model.generate_content(prompt)
    
    # Clean and parse JSON
    text = response.text.strip()
    text = re.sub(r'^```json\s*', '', text)
    text = re.sub(r'^```\s*', '', text)
    text = re.sub(r'\s*```$', '', text)
    
    return json.loads(text)

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/analyze")
async def analyze_resumes(
    job_description: str = Form(...),
    resumes: List[UploadFile] = File(...)
):
    if not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description is required")
    
    if not resumes or len(resumes) == 0:
        raise HTTPException(status_code=400, detail="At least one resume is required")
    
    if len(resumes) > 10:
        raise HTTPException(status_code=400, detail="Maximum 10 resumes allowed")
    
    # Extract text from all resumes
    resume_data = []
    for resume_file in resumes:
        content = await resume_file.read()
        text = extract_text_from_file(content, resume_file.filename)
        resume_data.append({
            "name": resume_file.filename.replace('.pdf', '').replace('.txt', ''),
            "filename": resume_file.filename,
            "text": text[:3000]  # Limit per resume to avoid token overflow
        })
    
    # Analyze with Gemini
    result = analyze_resumes_with_gemini(job_description, resume_data)
    
    return JSONResponse(content=result)

@app.get("/health")
async def health():
    return {"status": "healthy", "gemini_configured": bool(GEMINI_API_KEY)}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=7860, reload=False)
