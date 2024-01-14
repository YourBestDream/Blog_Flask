from flask import Blueprint, jsonify, request
from .models import Category, Tag, Post, Like, Bookmark
from flask_login import login_required, current_user
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
        post_list = []
        for post in posts:
            liked = Like.query.filter_by(user_id = current_user.id, post_id = post.id).first() is not None
            bookmarked = Bookmark.query.filter_by(user_id = current_user.id, post_id = post.id).first() is not None
            post_list.append({
                'id':post.id, 
                'title':post.title, 
                'category':db.session.execute(select(Category.name).where(Category.id == post.category_id)).scalar(),
                'date':post.updated_at.strftime('%d %b %Y %H:%M'), 
                'likes':post.likes,
                'bookmarks':post.bookmarks,
                'liked':liked,
                'bookmarked':bookmarked})
        return jsonify(post_list)

@requests.route('/add-like/<post_id>', methods=['POST','GET'])
@login_required
def add_like(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'error': 'Post not found'}), 404

    like = Like.query.filter_by(user_id=current_user.id, post_id=post_id).first()
    if like:
        db.session.delete(like)
        post.likes -= 1
    else:
        new_like = Like(user_id=current_user.id, post_id=post_id)
        db.session.add(new_like)
        post.likes += 1

    db.session.commit()
    return jsonify({'likes': post.likes}), 200

@requests.route('/add-bookmark/<post_id>', methods=['POST','GET'])
@login_required
def add_bookmark(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'error': 'Post not found'}), 404

    bookmark = Bookmark.query.filter_by(user_id=current_user.id, post_id=post_id).first()
    if bookmark:
        db.session.delete(bookmark)
        post.bookmarks -= 1
    else:
        new_bookmark = Bookmark(user_id=current_user.id, post_id=post_id)
        db.session.add(new_bookmark)
        post.bookmarks += 1

    db.session.commit()
    return jsonify({'bookmarks': post.bookmarks}), 200