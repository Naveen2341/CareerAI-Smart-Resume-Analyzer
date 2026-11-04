# CareerAI – Smart Resume Analyzer & Job Matcher

A full-stack web application built using **React.js and Python Django** that analyzes resumes and matches candidates with suitable job opportunities based on their skills.

##  Features

- User Registration and Login with JWT Authentication
- Upload resumes in PDF and DOCX formats
- Automatic resume text extraction
- Skill-based job matching
- Resume match percentage calculation
- Matched and missing skills identification
- Job recommendations
- Match history tracking
- Interactive React dashboard

##  Tech Stack

**Frontend**
- React.js
- JavaScript (ES6+)
- Redux Toolkit
- React Router
- Axios
- HTML5, CSS3

**Backend**
- Python
- Django
- Django REST Framework
- JWT Authentication

**Database**
- SQLite3

**Tools**
- VS Code
- Git and GitHub
- Postman

##  Project Structure

```text
CareerAI-Smart-Resume-Analyzer/
│
├── backend/
│   ├── accounts/
│   ├── analyzer/
│   ├── jobs/
│   ├── manage.py
│   └── requirements.txt
│
└── frontend/
    ├── src/
    ├── public/
    ├── package.json
    └── vite.config.js
```

##  Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Naveen2341/CareerAI-Smart-Resume-Analyzer.git
cd CareerAI-Smart-Resume-Analyzer
```

### 2. Backend Setup

```bash
cd backend
py -m venv venv
```

Activate the virtual environment on Windows:

```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the Django server:

```bash
python manage.py runserver
```

### 3. Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the application:

`http://localhost:5173`

##  How It Works

1. Register or log in to the application.
2. Upload your resume in PDF or DOCX format.
3. The backend extracts the resume content.
4. The application compares resume skills with job requirements.
5. It calculates a match percentage and identifies matched and missing skills.
6. View job recommendations and previous analysis results on the dashboard.

##  Future Enhancements

- NLP-based semantic resume matching
- AI-powered career recommendations
- Integration with external job listing APIs
- Advanced resume improvement suggestions

##  Author

**Naveen2341**

GitHub: https://github.com/Naveen2341

---

