# CareerAI – Smart Resume Analyzer & Job Matcher

CareerAI is a full-stack portfolio application that lets a user upload a PDF/DOCX resume, extract its text, compare it with job descriptions, calculate an explainable keyword-match score, identify missing skills, and save job matches.

## Technology
- Frontend: React 18, JavaScript ES6+, Vite, React Router, Axios, Recharts, Lucide React
- Backend: Python 3.10+, Django 5, Django REST Framework
- Database: SQLite3
- Resume parsing: PyMuPDF (PDF), python-docx (DOCX)
- Authentication: JWT (Simple JWT)
- No WebSockets. The app uses ordinary HTTP REST API requests.

## Features
- Register/login with JWT authentication
- Upload PDF or DOCX resume
- Extract resume text on the backend
- Add and browse job descriptions
- Match a resume against a job using skill/keyword overlap
- Show match percentage, matched skills, missing skills and recommendations
- Save/bookmark jobs and view match history
- Dashboard with charts and summary statistics

> The matching score is a transparent keyword/skill overlap heuristic, not an AI/LLM judgement or a guarantee of interview selection. It can be extended with embeddings or an LLM later.

## Requirements
- Python 3.10+
- Node.js 18+
- Git

## Backend setup (Windows PowerShell)
```powershell
cd backend
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations accounts analyzer jobs
python manage.py migrate
python manage.py runserver
```
Backend: http://127.0.0.1:8000/

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal, then activate again.

## Frontend setup (second terminal)
```bash
cd frontend
npm install
npm run dev
```
Frontend: http://localhost:5173/

## Quick demo
1. Register a new account.
2. Upload a PDF/DOCX resume from the Resume page.
3. Open Jobs and add a job description (or use the sample jobs button).
4. Open a job and click **Analyze match**.
5. Review the score, matched skills, missing skills and suggestions.
6. Save jobs and inspect your dashboard.

## API routes
| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/auth/register/` | Create account |
| POST | `/api/auth/token/` | Obtain JWT pair |
| POST | `/api/auth/token/refresh/` | Refresh access token |
| GET | `/api/auth/me/` | Current user |
| GET/POST | `/api/resumes/` | List/upload resumes |
| GET/DELETE | `/api/resumes/{id}/` | Resume detail/delete |
| GET/POST | `/api/jobs/` | List/create jobs |
| GET/PATCH/DELETE | `/api/jobs/{id}/` | Job detail/update/delete |
| POST | `/api/jobs/{id}/save/` | Toggle saved job |
| POST | `/api/matches/analyze/` | Analyze resume vs job |
| GET | `/api/matches/` | Current user's match history |
| GET | `/api/dashboard/` | Dashboard statistics |

## GitHub upload
Create an empty repository named `CareerAI-Smart-Resume-Analyzer`, extract this ZIP, open a terminal in the extracted project folder and run:
```bash
git init
git add .
git commit -m "Initial commit: CareerAI Smart Resume Analyzer"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/CareerAI-Smart-Resume-Analyzer.git
git push -u origin main
```
Replace `YOUR-USERNAME` with your GitHub username.

## Suggested repository description
A full-stack smart resume analyzer and job matcher built with React, JavaScript, Django REST Framework and SQLite3. Includes resume parsing, explainable skill matching, missing-skill insights, saved jobs and analytics.

## Interview explanation
"I built CareerAI, a full-stack resume analysis and job matching platform. The React frontend communicates with Django REST APIs. Users upload PDF or DOCX resumes; the backend extracts text and compares resume skills with job requirements using a transparent weighted keyword-matching approach. The application shows a match score, matched and missing skills, and actionable recommendations. Django REST Framework handles APIs and JWT authentication, while SQLite3 stores users, resumes, jobs, saved jobs and match history."

## Important notes
- Uploaded resumes are private to the authenticated user through API permissions. For a public deployment, configure private media storage, file-size limits, malware scanning, HTTPS and secure secrets.
- The sample keyword matcher is rule-based. Do not describe it as a trained machine-learning model or generative AI system.
- Set `DEBUG=False`, use environment variables for secrets, configure `ALLOWED_HOSTS`, and review media storage/security before deployment.
