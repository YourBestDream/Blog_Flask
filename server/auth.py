from .models import User
from . import db

from uuid import uuid4
from flask import Blueprint, jsonify, request, redirect
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth',__name__)

@auth.route('/signup',methods = ['GET','POST'])
def signup():
    if methods == 'POST':
        email = request.json.get('email')
        first_name = request.json.get('firstName')
        last_name = request.json.get('lastName')
        password = request.json.get('password')
        user = User.query.filter_by(email = email).first()
        if user:
            return jsonify({"error": "User already exists"}), 409
        else:
            new_user = User(id = str(uuid4()),email = email, password = generate_password_hash(password, method='pbkdf2'), first_name = first_name, last_name = last_name)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember = True)
        
        return jsonify("Suck chess")

@auth.route('/login', methods = ['GET','POST'])
def login():
    if methods == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400

        user = User.query.filter_by(email = email).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return jsonify({"message": "Login successful"}), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401 