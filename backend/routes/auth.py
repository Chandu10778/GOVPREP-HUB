from flask import Blueprint, request, jsonify
from models import db, User

auth = Blueprint('auth', __name__)

# REGISTER
@auth.route('/register', methods=['POST'])
def register():
    data = request.json

    # Check if user exists
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    user = User(
        name=data['name'],
        email=data['email'],
        password=data['password']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully",
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
        "level": user.level,
        "xp": user.xp,
        "streak": user.streak,
    })

# LOGIN
@auth.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(
        email=data['email'],
        password=data['password']
    ).first()

    if user:
        return jsonify({
            "message": "Login successful",
            "user_id": user.id,
            "name": user.name,
            "email": user.email,
            "level": user.level,
            "xp": user.xp,
            "streak": user.streak,
        })
    else:
        return jsonify({"message": "Invalid credentials"}), 401