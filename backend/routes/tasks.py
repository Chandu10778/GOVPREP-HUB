from flask import Blueprint, jsonify, request
from models import db, Task

tasks = Blueprint('tasks', __name__)

STAGE_NAMES = {
    1: 'Beginner',
    2: 'Basics Completed',
    3: 'Intermediate',
    4: 'Advanced',
    5: 'Exam Ready'
}

# GET TASKS BY STAGE
@tasks.route('/tasks/stage/<int:stage>', methods=['GET'])
def get_tasks_by_stage(stage):
    task_list = Task.query.filter_by(stage=stage).all()
    return jsonify([
        {
            'id': t.id,
            'title': t.title,
            'subject': t.subject,
            'description': t.description,
            'xp': t.xp,
            'stage': t.stage,
            'stage_name': STAGE_NAMES.get(t.stage, 'Unknown')
        } for t in task_list
    ])

# GET TASKS BY SUBJECT
@tasks.route('/tasks/subject/<string:subject>', methods=['GET'])
def get_tasks_by_subject(subject):
    task_list = Task.query.filter_by(subject=subject.title()).all()
    return jsonify([
        {
            'id': t.id,
            'title': t.title,
            'subject': t.subject,
            'description': t.description,
            'xp': t.xp,
            'stage': t.stage,
            'stage_name': STAGE_NAMES.get(t.stage, 'Unknown')
        } for t in task_list
    ])

# CREATE TASK
@tasks.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    title = data.get('title')
    subject = data.get('subject')
    description = data.get('description', '')
    xp = data.get('xp')
    stage = data.get('stage')

    if not title or not subject or xp is None or stage is None:
        return jsonify({"message": "title, subject, xp, and stage are required"}), 400

    try:
        xp = int(xp)
        stage = int(stage)
    except (ValueError, TypeError):
        return jsonify({"message": "xp and stage must be integers"}), 400

    task = Task(title=title.strip(), subject=subject.title().strip(), description=description.strip(), xp=xp, stage=stage)
    db.session.add(task)
    db.session.commit()

    return jsonify({
        "message": "Task created",
        "task": {
            "id": task.id,
            "title": task.title,
            "subject": task.subject,
            "description": task.description,
            "xp": task.xp,
            "stage": task.stage,
            "stage_name": STAGE_NAMES.get(task.stage, 'Unknown')
        }
    }), 201