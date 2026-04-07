# 🔬 TalentLens AI — Resume Screener & Ranker

<div align="center">

![TalentLens Banner](https://img.shields.io/badge/TalentLens-AI%20Resume%20Screener-blue?style=for-the-badge&logo=google&logoColor=white)

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Hugging%20Face-yellow?style=for-the-badge)](https://huggingface.co/spaces/prasanthr0416/talentlens-ai)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-orange?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

**An AI-powered HR tool that screens, scores, and ranks candidates by analyzing resumes against job descriptions using Google Gemini 2.5 Flash.**

[🚀 Live Demo](https://huggingface.co/spaces/prasanthr0416/talentlens-ai)

</div>

---

## ✨ Features

- 📄 **Multi-Resume Upload** — Upload up to 10 PDF or TXT resumes at once
- 🧠 **Gemini 2.5 Flash AI** — Deep semantic analysis beyond keyword matching
- 📊 **4-Axis Scoring** — Experience, Skills, Education & Culture Fit scored out of 100
- 🏆 **Smart Ranking** — Candidates ranked from best to worst fit with reasoning
- 💬 **Interview Questions** — 3 tailored interview questions generated per candidate
- ✅ **Skills Gap Analysis** — Matched vs missing skills highlighted clearly
- 💡 **Hiring Recommendation** — AI explains exactly why to hire or pass
- 🎨 **Super Dark UI** — Animated futuristic interface with score rings & expandable cards
- 🐳 **Docker Ready** — One command deployment anywhere

---

## 🖥️ Demo

<div align="center">

| Feature | Preview |
|---|---|
| 🏠 Home Screen | Dark futuristic UI with drag & drop upload |
| 📊 Results | Ranked candidates with animated score rings |
| 🔍 Detail View | Full breakdown with skills, strengths & questions |

👉 **[Try it live on Hugging Face Spaces](https://huggingface.co/spaces/prasanthr0416/talentlens-ai)**

</div>

---

## 🏗️ How It Works

```
User uploads JD + Resumes
         ↓
FastAPI receives files
         ↓
PyPDF2 extracts text from PDFs
         ↓
Gemini 2.5 Flash analyzes all resumes against JD
         ↓
AI scores each candidate on 4 axes
         ↓
Results ranked & displayed with full reasoning
```

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI + Python 3.11 |
| **AI Model** | Google Gemini 2.5 Flash |
| **PDF Parsing** | PyPDF2 |
| **Frontend** | Vanilla HTML + CSS + JS (no framework!) |
| **Deployment** | Docker + Hugging Face Spaces |
| **Font** | Syne + DM Sans + JetBrains Mono |

---

## ⚙️ Setup

### Prerequisites
- Python 3.11+
- Google Gemini API Key → [Get free key here](https://aistudio.google.com)

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/talentlens-ai.git
cd talentlens-ai
```

### 2. Create virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Open `app.py` and replace line 17:

```python
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
```

### 5. Run the app

```bash
uvicorn app:app --reload --port 8000
```

### 6. Open in browser

```
http://localhost:8000
```

---

## 🐳 Deployment

### Deploy to Hugging Face Spaces

1. **Create a new Space** at [huggingface.co/spaces](https://huggingface.co/spaces)
   - SDK: **Docker**

2. **Add Secret** in Space Settings:
   - Name: `GEMINI_API_KEY`
   - Value: your Gemini API key

3. **Push code:**

```bash
git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
git push origin master:main
```

4. Wait ~3 minutes for build → Your app is live! 🎉

---

## 📁 Project Structure

```
talentlens-ai/
├── app.py                  ← FastAPI backend (all logic)
├── requirements.txt        ← Python dependencies
├── Dockerfile              ← Docker config for HF Spaces
├── README.md               ← You are here!
├── .gitignore              ← Ignores venv, pycache etc
├── static/                 ← Static files folder
│   └── .gitkeep
└── templates/
    └── index.html          ← Full frontend UI
```

---

## 📊 Scoring System

Each candidate is scored across 4 dimensions:

| Dimension | What AI Evaluates |
|---|---|
| **Experience Score** | Years of experience, role relevance, industry match |
| **Skills Score** | Technical skills matched vs required in JD |
| **Education Score** | Degree level, field of study, certifications |
| **Culture Fit Score** | Soft skills, communication style, team fit signals |

### Verdict Labels

| Score | Verdict | Meaning |
|---|---|---|
| 80–100 | 🟢 Strong Match | Highly recommended to interview |
| 60–79 | 🔵 Good Match | Worth interviewing |
| 40–59 | 🟡 Partial Match | Has potential but gaps exist |
| 0–39 | 🔴 Weak Match | Significant misalignment |

---

## 🔑 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GEMINI_API_KEY` | ✅ Yes | Google Gemini API key from [aistudio.google.com](https://aistudio.google.com) |

---

## 📦 Dependencies

```
fastapi==0.111.0
uvicorn==0.29.0
python-multipart==0.0.9
google-generativeai==0.7.0
PyPDF2==3.0.1
```

---

## 🚀 Future Improvements

- [ ] Add support for DOCX resumes
- [ ] Export results as PDF report
- [ ] Email shortlisted candidates directly
- [ ] ATS (Applicant Tracking System) integration
- [ ] Batch processing with progress bar
- [ ] Save & compare results across sessions

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Prasanth R**
- 🤗 Hugging Face: [@prasanthr0416](https://huggingface.co/prasanthr0416)
- 💼 Built as part of AI Engineer Portfolio Projects

---

<div align="center">

**Built with ❤️ using Gemini 2.5 Flash + FastAPI**

⭐ Star this repo if you found it helpful!

</div>
