# Student Smart Hub

**One platform. Smart academics.**

A fully animated, modern, responsive educational web platform for students and faculty — glassmorphism + neumorphism, gradient accents (Blue → Purple → Teal), dark/light mode, and AI assistant (OpenAI).

## Quick Start

```bash
cd student-smart-hub
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

Create a `.env` file (copy from `.env.example`):

- `OPENAI_API_KEY` — Your OpenAI API key for AI assistant (optional; works in demo mode without it)

Run:

```bash
python app.py
```

Open **http://127.0.0.1:5000**

## Demo Logins

- **Student:** `student@hub.com` or `2024001` — password: `student123`
- **Faculty:** `faculty@hub.com` or `F001` — password: `faculty123`

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **AI:** OpenAI API (optional)

## Features

- Landing page with role selection (Student / Faculty)
- Student & Faculty login
- Student portal: Dashboard, Profile, Assignments, Timetable, Exams, Attendance, Notes, Video, AI Assistant, Planner, Notifications, Gamification, Analytics, Settings
- Faculty portal: Dashboard, Student Management, Assignments, Attendance, Exams & Analytics, Communication, AI Teaching Assistant, Settings
- AI chat for students and faculty (OpenAI); demo replies when no API key

---

*Student Smart Hub is not just an LMS. It's a smart academic companion that centralizes learning, automates academic tracking, and uses AI to support both students and faculty in real time.*
