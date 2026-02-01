"""
Student Smart Hub - Flask Backend
One platform. Smart academics.
"""
import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from functools import wraps
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'student-smart-hub-secret-key-2024')

# OpenAI: set OPENAI_API_KEY in .env to enable AI assistant

# Mock users for demo (in production use DB)
STUDENTS = {'student@hub.com': 'student123', '2024001': 'student123'}
FACULTY = {'faculty@hub.com': 'faculty123', 'F001': 'faculty123'}

def student_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('student_logged_in'):
            return redirect(url_for('student_login'))
        return f(*args, **kwargs)
    return decorated

def faculty_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('faculty_logged_in'):
            return redirect(url_for('faculty_login'))
        return f(*args, **kwargs)
    return decorated

# ============ LANDING & LOGIN ============
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student-login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        data = request.get_json() or request.form
        uid = (data.get('email') or data.get('roll_no') or '').strip()
        pwd = data.get('password', '')
        if uid in STUDENTS and STUDENTS[uid] == pwd:
            session['student_logged_in'] = True
            session['student_id'] = uid
            return jsonify({'success': True, 'redirect': url_for('student_dashboard')})
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
    return render_template('student_login.html')

@app.route('/faculty-login', methods=['GET', 'POST'])
def faculty_login():
    if request.method == 'POST':
        data = request.get_json() or request.form
        uid = (data.get('email') or data.get('faculty_id') or '').strip()
        pwd = data.get('password', '')
        if uid in FACULTY and FACULTY[uid] == pwd:
            session['faculty_logged_in'] = True
            session['faculty_id'] = uid
            return jsonify({'success': True, 'redirect': url_for('faculty_dashboard')})
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
    return render_template('faculty_login.html')

@app.route('/logout/student')
def student_logout():
    session.pop('student_logged_in', None)
    session.pop('student_id', None)
    return redirect(url_for('index'))

@app.route('/logout/faculty')
def faculty_logout():
    session.pop('faculty_logged_in', None)
    session.pop('faculty_id', None)
    return redirect(url_for('index'))

# ============ STUDENT PORTAL ============
@app.route('/student/dashboard')
@student_required
def student_dashboard():
    return render_template('student_dashboard.html')

@app.route('/student/profile')
@student_required
def student_profile():
    return render_template('student_profile.html')

# ============ FACULTY PORTAL ============
@app.route('/faculty/dashboard')
@faculty_required
def faculty_dashboard():
    return render_template('faculty_dashboard.html')

# ============ AI ASSISTANT API ============
@app.route('/api/ai/chat', methods=['POST'])
def ai_chat():
    """OpenAI-powered chat for students and faculty."""
    data = request.get_json() or {}
    message = (data.get('message') or '').strip()
    role = data.get('role', 'student')
    if not message:
        return jsonify({'reply': 'Please enter a message.'}), 400
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key or api_key == 'sk-placeholder':
        return jsonify({
            'reply': "AI is not configured. Set OPENAI_API_KEY in .env to enable. For demo: I'm your academic assistant. Ask about assignments, DBMS normalization, or study tips!"
        })
    try:
        client = OpenAI(api_key=api_key)
        system = (
            "You are a helpful academic assistant for Student Smart Hub. "
            "Help with assignments, explain concepts (e.g. DBMS normalization), study tips, and academic queries. "
            "Be concise and professional."
        )
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': system},
                {'role': 'user', 'content': message}
            ],
            max_tokens=400,
            temperature=0.7
        )
        reply = response.choices[0].message.content
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({
            'reply': f"AI service temporarily unavailable. (Error: {str(e)[:80]}) Try again or use demo mode."
        }), 500

# ============ MOCK DATA APIs (optional) ============
@app.route('/api/student/dashboard-data')
@student_required
def student_dashboard_data():
    return jsonify({
        'upcoming_assignments': [
            {'subject': 'DBMS', 'due': '2024-02-05', 'title': 'Normalization Assignment'},
            {'subject': 'DSA', 'due': '2024-02-08', 'title': 'Tree Traversal'}
        ],
        'next_class': {'subject': 'DBMS', 'time': '10:00 AM', 'room': 'Room 301'},
        'attendance_percent': 87,
        'cgpa': 8.4,
        'notifications': [
            {'text': 'Assignment due in 3 days', 'time': '2h ago'},
            {'text': 'New material uploaded', 'time': '5h ago'}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
