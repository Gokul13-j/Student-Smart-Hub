# Student Smart Hub 

## Problem Statement
Students often miss assignments, exams, and important updates because
academic information is scattered across WhatsApp groups, emails,
and notice boards.

Student Smart Hub solves this by providing a centralized,
AI-powered academic dashboard.


## Architecture
![Architecture](architecture/architecture.png)

User → Frontend (HTML/CSS/JS)  
→ Flask Backend  
→ OpenAI API


## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- AI: OpenAI API
- Environment: python-dotenv

## AI Tools Used
- OpenAI API
- ChatGPT for debugging

## Prompt Strategy Summary
We used structured prompt templates to ensure consistent and relevant
AI responses. Prompts were designed with clear instructions and
context-aware inputs.

## Setup Instructions (Build Reproducibility)

1. Clone the repository  
   `git clone <repo-link>`

2. Navigate to project folder  
   `cd student-smart-hub`

3. Create virtual environment  
   `python -m venv venv`

4. Activate venv  
   **Windows:** `venv\Scripts\activate`

5. Install dependencies  
   `pip install -r requirements.txt`

6. Create environment file  
   Copy `.env.example` → `.env`  
   Add your OpenAI API key

7. Run the application  
   `python app.py`

8. Open in browser  
   `http://127.0.0.1:5000`

## Final Output
- Centralized student dashboard
- AI-powered academic assistance
- Clean and user-friendly interface

## Build Reproducibility
This project can be fully reproduced using the above steps
and the provided requirements.txt file.
