from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

# 👤 User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    level = db.Column(db.Integer, default=1)
    xp = db.Column(db.Integer, default=0)
    streak = db.Column(db.Integer, default=0)

# 📚 Subject-based Study Task Table
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, default='')
    stage = db.Column(db.Integer, nullable=False, default=1)
    xp = db.Column(db.Integer, nullable=False, default=10)

# 📊 Progress Table
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    task_id = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, default=False)

# 🔎 Subject Progress Table
class SubjectProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    completed_tasks = db.Column(db.Integer, default=0)
    xp = db.Column(db.Integer, default=0)

# 🧾 Previous Year Question (PYQ) Table
class PYQQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    question = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text, nullable=False)  # JSON string
    answer = db.Column(db.String(200), nullable=False)
    xp = db.Column(db.Integer, default=20)

# ✅ PYQ Attempt Table
class PYQAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    pyq_id = db.Column(db.Integer, nullable=False)
    selected_option = db.Column(db.String(200), nullable=False)
    correct = db.Column(db.Boolean, nullable=False)
    xp_gained = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, default=func.now())

# 📖 Study Materials Table
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)  # HTML/Rich text content
    level = db.Column(db.String(50), default='Beginner')  # Beginner, Intermediate, Advanced
    xp_reward = db.Column(db.Integer, default=15)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

# 📚 Material Progress Table (tracks which materials users have read)
class MaterialProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    material_id = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    xp_earned = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, default=func.now())