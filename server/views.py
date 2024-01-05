from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
import json

views = Blueprint('views',__name__)

@views.route('/home',methods = ['GET','POST'])
def homepage(): 
    return jsonify({'text':'I am your father'})

@views.route('/post', methods = ['GET','POST'])
def post_creation():
    if methods == 'GET':
        return jsonify({'message':'suck chess'})
    elif methods == 'POST':
        return jsonify({'message':'created'})