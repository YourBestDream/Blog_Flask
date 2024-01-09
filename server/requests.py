from flask import Blueprint, jsonify, request
from .models import Category, Tag
from . import db
from sqlalchemy import select
import json

requests = Blueprint('requests',__name__)

@requests.route('/tags', methods = ['GET'])
def tag_retrieve():
    if request.method == 'GET':
        tags = db.session.execute(select(Tag)).scalars().all()
        tag_list = [{'id':tag.id, 'name':tag.name} for tag in tags]
        return jsonify(tag_list)

@requests.route('/categories', methods = ['GET'])
def categories_retrieve():
    if request.method == 'GET':
        cats = db.session.execute(select(Category)).scalars().all()
        cats_list = [{'id':cat.id, 'name':cat.name} for cat in cats]
        return jsonify(cats_list)