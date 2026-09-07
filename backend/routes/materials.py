from flask import Blueprint, jsonify, request
from models import db, Material, MaterialProgress, User

materials = Blueprint('materials', __name__)

SUBJECTS = ['Polity', 'History', 'Geography', 'Current Affairs', 'Quantitative Aptitude']

# GET ALL SUBJECTS
@materials.route('/subjects', methods=['GET'])
def get_subjects():
    return jsonify({'subjects': SUBJECTS})

# GET MATERIALS BY SUBJECT
@materials.route('/materials/<subject>', methods=['GET'])
def get_materials_by_subject(subject):
    try:
        material_list = Material.query.filter_by(subject=subject).all()
        return jsonify([
            {
                'id': m.id,
                'title': m.title,
                'subject': m.subject,
                'level': m.level,
                'xp_reward': m.xp_reward,
                'created_at': m.created_at.strftime('%Y-%m-%d') if m.created_at else None
            } for m in material_list
        ])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# GET SINGLE MATERIAL CONTENT
@materials.route('/materials/content/<int:material_id>', methods=['GET'])
def get_material_content(material_id):
    try:
        material = Material.query.get(material_id)
        if not material:
            return jsonify({'error': 'Material not found'}), 404
        
        return jsonify({
            'id': material.id,
            'title': material.title,
            'subject': material.subject,
            'content': material.content,
            'level': material.level,
            'xp_reward': material.xp_reward,
            'created_at': material.created_at.strftime('%Y-%m-%d') if material.created_at else None
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# CREATE NEW MATERIAL (Admin/System use)
@materials.route('/materials', methods=['POST'])
def create_material():
    try:
        data = request.json
        
        if not data.get('title') or not data.get('subject') or not data.get('content'):
            return jsonify({'error': 'Missing required fields: title, subject, content'}), 400
        
        material = Material(
            title=data.get('title'),
            subject=data.get('subject'),
            content=data.get('content'),
            level=data.get('level', 'Beginner'),
            xp_reward=data.get('xp_reward', 15)
        )
        
        db.session.add(material)
        db.session.commit()
        
        return jsonify({
            'message': 'Material created successfully',
            'material_id': material.id,
            'title': material.title
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# UPDATE MATERIAL PROGRESS (Mark as completed/read)
@materials.route('/materials/progress', methods=['POST'])
def update_material_progress():
    try:
        data = request.json
        user_id = data.get('user_id')
        material_id = data.get('material_id')
        
        if not user_id or not material_id:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Check if user exists
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        # Check if material exists
        material = Material.query.get(material_id)
        if not material:
            return jsonify({'error': 'Material not found'}), 404
        
        # Check if progress already exists
        progress = MaterialProgress.query.filter_by(
            user_id=user_id,
            material_id=material_id
        ).first()
        
        if progress:
            progress.completed = True
            progress.xp_earned = material.xp_reward
        else:
            progress = MaterialProgress(
                user_id=user_id,
                material_id=material_id,
                completed=True,
                xp_earned=material.xp_reward
            )
            db.session.add(progress)
        
        # Award XP to user
        user.xp += material.xp_reward
        
        db.session.commit()
        
        return jsonify({
            'message': 'Progress updated successfully',
            'xp_earned': material.xp_reward,
            'total_xp': user.xp
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# GET USER'S MATERIAL PROGRESS
@materials.route('/user/<int:user_id>/material-progress', methods=['GET'])
def get_user_material_progress(user_id):
    try:
        progress_list = MaterialProgress.query.filter_by(user_id=user_id).all()
        return jsonify([
            {
                'material_id': p.material_id,
                'completed': p.completed,
                'xp_earned': p.xp_earned,
                'timestamp': p.timestamp.strftime('%Y-%m-%d') if p.timestamp else None
            } for p in progress_list
        ])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# GET MATERIALS BY SUBJECT WITH USER PROGRESS
@materials.route('/materials/<subject>/user/<int:user_id>', methods=['GET'])
def get_materials_with_progress(subject, user_id):
    try:
        material_list = Material.query.filter_by(subject=subject).all()
        completed_ids = [p.material_id for p in MaterialProgress.query.filter_by(
            user_id=user_id, 
            completed=True
        ).all()]
        
        return jsonify([
            {
                'id': m.id,
                'title': m.title,
                'subject': m.subject,
                'level': m.level,
                'xp_reward': m.xp_reward,
                'completed': m.id in completed_ids,
                'created_at': m.created_at.strftime('%Y-%m-%d') if m.created_at else None
            } for m in material_list
        ])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
