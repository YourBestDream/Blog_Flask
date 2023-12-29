from .model import User
from . import db

from flask import Blueprint, jsonify, request, redirect
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth',__name__)

