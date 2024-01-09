from flask import Blueprint, jsonify, request
from .models import Category, Tag, Post
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

@requests.route('/posts-retrieve', methods=['GET'])
def posts_retrieve():
    if request.method == 'GET':
        posts = db.session.execute(select(Post)).scalars().all()
        post_list = [{'id':post.id, 'title':post.title, 'content':post.text,'date':post.updated_at.strftime('%d %b %Y')} for post in posts]
        return jsonify(post_list)