import json
import os
import re
import urllib.error
import urllib.request

from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from models import db, User, Task, Progress, SubjectProgress, PYQQuestion, PYQAttempt, Material
from config import Config

user = Blueprint('user', __name__)


def strip_html_tags(text):
    if not text:
        return ''
    return re.sub(r'<[^>]+>', '', text)


def material_preview(material):
    preview_text = strip_html_tags(material.content)
    preview_text = ' '.join(preview_text.split())
    if len(preview_text) > 400:
        preview_text = preview_text[:400].rsplit(' ', 1)[0] + '...'
    return f"{material.title}: {preview_text}"

STAGE_NAMES = {
    1: 'Beginner',
    2: 'Basics Completed',
    3: 'Intermediate',
    4: 'Advanced',
    5: 'Exam Ready'
}


def update_user_stage(user):
    # total XP thresholds for stage leveling
    if user.xp >= 400:
        user.level = 5
        user.xp = min(user.xp, 499)
    elif user.xp >= 300:
        user.level = 4
    elif user.xp >= 200:
        user.level = 3
    elif user.xp >= 100:
        user.level = 2
    else:
        user.level = 1


# COMPLETE TASK
@user.route('/complete-task', methods=['POST'])
def complete_task():
    data = request.json

    user_obj = User.query.get(data.get('user_id'))
    task = Task.query.get(data.get('task_id'))

    if not user_obj or not task:
        return jsonify({"message": "Invalid user or task"}), 400

    user_obj.xp += task.xp
    user_obj.streak = user_obj.streak + 1 if user_obj.streak is not None else 1

    # cumulative experience and stage update
    update_user_stage(user_obj)

    # Save task-level progress
    progress = Progress(user_id=user_obj.id, task_id=task.id, completed=True)
    db.session.add(progress)

    # Save subject-level progress
    subject_progress = SubjectProgress.query.filter_by(user_id=user_obj.id, subject=task.subject).first()
    if not subject_progress:
        subject_progress = SubjectProgress(user_id=user_obj.id, subject=task.subject, completed_tasks=0, xp=0)
    subject_progress.completed_tasks += 1
    subject_progress.xp += task.xp
    db.session.add(subject_progress)

    db.session.commit()

    return jsonify({
        "message": "Task completed",
        "new_level": user_obj.level,
        "stage_name": STAGE_NAMES.get(user_obj.level, 'Unknown'),
        "xp": user_obj.xp,
        "streak": user_obj.streak
    })


# LEADERBOARD
@user.route('/leaderboard', methods=['GET'])
def leaderboard():
    leaders = User.query.order_by(User.level.desc(), User.xp.desc()).limit(10).all()
    return jsonify([{
        "user_id": u.id,
        "username": u.name,
        "level": u.level,
        "stage_name": STAGE_NAMES.get(u.level, 'Unknown'),
        "xp": u.xp,
        "streak": u.streak
    } for u in leaders])


# SUBJECT PROGRESS
@user.route('/user/<int:user_id>/progress', methods=['GET'])
def user_progress(user_id):
    progress = SubjectProgress.query.filter_by(user_id=user_id).all()
    return jsonify([{ 'subject': p.subject, 'completed_tasks': p.completed_tasks, 'xp': p.xp } for p in progress])


# PYQ QUESTIONS
@user.route('/pyq', methods=['GET'])
def get_pyq_questions():
    subject = request.args.get('subject')
    query = PYQQuestion.query
    if subject:
        query = query.filter_by(subject=subject.title())
    questions = query.all()

    return jsonify([{ 'id': q.id, 'subject': q.subject, 'question': q.question, 'options': q.options, 'xp': q.xp } for q in questions])


@user.route('/pyq', methods=['POST'])
def add_pyq_question():
    data = request.json
    subject = data.get('subject')
    question = data.get('question')
    options = data.get('options')
    answer = data.get('answer')
    xp = data.get('xp', 20)

    if not subject or not question or not options or not answer:
        return jsonify({"message": "subject, question, options, and answer are required"}), 400

    new_q = PYQQuestion(subject=subject.title(), question=question, options=options, answer=answer, xp=int(xp))
    db.session.add(new_q)
    db.session.commit()

    return jsonify({"message": "PYQ created", 'pyq_id': new_q.id}), 201


@user.route('/pyq/answer', methods=['POST'])
def answer_pyq():
    data = request.json
    user_obj = User.query.get(data.get('user_id'))
    pyq_id = data.get('pyq_id')
    selected_option = data.get('selected_option')

    if not user_obj or not pyq_id or selected_option is None:
        return jsonify({"message": "user_id, pyq_id, and selected_option are required"}), 400

    pyq = PYQQuestion.query.get(pyq_id)
    if not pyq:
        return jsonify({"message": "Invalid PYQ question"}), 400

    correct = (str(selected_option).strip().lower() == str(pyq.answer).strip().lower())
    xp_gained = pyq.xp if correct else max(1, int(pyq.xp * 0.25))

    # update user XP and stage
    user_obj.xp += xp_gained
    update_user_stage(user_obj)

    attempt = PYQAttempt(user_id=user_obj.id, pyq_id=pyq.id, selected_option=selected_option, correct=correct, xp_gained=xp_gained)
    db.session.add(attempt)

    # Add to subject progress
    subject_progress = SubjectProgress.query.filter_by(user_id=user_obj.id, subject=pyq.subject).first()
    if not subject_progress:
        subject_progress = SubjectProgress(user_id=user_obj.id, subject=pyq.subject, completed_tasks=0, xp=0)
    subject_progress.xp += xp_gained
    if correct:
        subject_progress.completed_tasks += 1
    db.session.add(subject_progress)

    db.session.commit()

    return jsonify({
        'correct': correct,
        'xp_gained': xp_gained,
        'new_level': user_obj.level,
        'stage_name': STAGE_NAMES.get(user_obj.level, 'Unknown'),
        'xp': user_obj.xp
    })


# ENHANCED CHATBOT (with comprehensive knowledge base)
@user.route('/chat', methods=['POST'])
def chatbot():
    data = request.json
    question = (data.get('question') or '').strip()

    if not question:
        return jsonify({'reply': 'Please ask a study question to get help.', 'answer': 'Please ask a study question to get help.'}), 400

    # Use Mistral AI API for chatbot
    try:
        api_key = "cqfapVPeJNXgCqCrfkPEosduo24N7Pk0"
        url = "https://api.mistral.ai/v1/chat/completions"
        system_prompt = "You are ExamBot, an expert AI study assistant. Answer every question the user asks clearly and helpfully. You specialize in exam preparation for UPSC, JEE, NEET, and other competitive exams, but you should still respond to any general question with a useful answer. You provide: Clear explanations of complex concepts, Study tips and strategies, Connections between topics, Practice advice, Motivation and guidance. Keep responses focused, easy to understand, and use examples when helpful."
        payload = json.dumps({
            "model": "mistral-medium",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            "temperature": 0.7,
            "max_tokens": 600
        }).encode('utf-8')
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        request_obj = urllib.request.Request(url, data=payload, headers=headers, method='POST')
        with urllib.request.urlopen(request_obj, timeout=30) as resp:
            resp_text = resp.read().decode('utf-8')
            data = json.loads(resp_text)
        answer_text = None
        if isinstance(data, dict):
            if 'choices' in data and len(data['choices']) > 0:
                first_choice = data['choices'][0]
                if isinstance(first_choice, dict):
                    if 'message' in first_choice and isinstance(first_choice['message'], dict):
                        answer_text = first_choice['message'].get('content')
                    elif 'text' in first_choice:
                        answer_text = first_choice.get('text')
        if answer_text:
            return jsonify({'reply': answer_text.strip(), 'answer': answer_text.strip()})
        else:
            return jsonify({'reply': 'No answer from Mistral API.', 'answer': 'No answer from Mistral API.'}), 500
    except urllib.error.HTTPError as e:
        return jsonify({'reply': f'Mistral API error: {e.code}', 'answer': f'Mistral API error: {e.code}'}), 500
    except Exception as e:
        return jsonify({'reply': f'Mistral API error: {str(e)}', 'answer': f'Mistral API error: {str(e)}'}), 500


# TEXT SUMMARIZATION (simple extractive)
@user.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.json
    text = (data.get('text') or '').strip()

    if not text:
        return jsonify({'summary': ''}), 400

    sentences = [s.strip() for s in text.replace('\n', ' ').split('.') if s.strip()]
    if not sentences:
        return jsonify({'summary': text[:300] + ('...' if len(text) > 300 else '')})

    limit = min(3, len(sentences))
    summary = '. '.join(sentences[:limit])
    if len(summary) < len(text):
        summary += '...'
    return jsonify({'summary': summary})