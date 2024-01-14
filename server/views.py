from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from . import db
from sqlalchemy import select
from .models import Post, Category, Tag
from uuid import uuid4

import json

views = Blueprint('views',__name__)

@views.route('/post', methods = ['GET','POST'])
@login_required
def post_creation():
    if request.method == 'GET':
        return jsonify({'message':'suck chess'})

    elif request.method == 'POST':
        title = request.json.get('title')
        text = request.json.get('content')
        cat = request.json.get('category')
        tags = request.json.get('tags')
        
        if not title or not text or not cat:
            return jsonify({'error': 'Missing data'}), 400
        
        if not current_user.is_authenticated:
            return jsonify({'error': 'User not logged in'}), 401

        category = db.session.execute(select(Category).filter_by(name = cat)).scalars().first()
        
        new_post = Post(id = uuid4(), title = title, text = text, likes = 0, bookmarks = 0,created_by = current_user.id, category_id = category.id)

        for tag_name in tags:
            tag = db.session.execute(select(Tag).filter_by(name=tag_name)).scalars().first()
            if not tag:
                tag = Tag(name=tag_name)  # Create new tag if it doesn't exist
                db.session.add(tag)
            new_post.tags.append(tag)  # Associate the tag with the post
        
        db.session.add(new_post)
        db.session.commit()

        return jsonify({'message':'created'}), 201

    else:

        return jsonify({'message':'Invalid request method'}), 405