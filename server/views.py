from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
import json

views = Blueprint('views',__name__)

@views.route('/',methods = ['GET','POST'])
def homepage():
    return jsonify({'text':'I am your father'})