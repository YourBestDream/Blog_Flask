from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.String(36), primary_key = True, nullable = False)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone = True), default = func.now(), nullable = False)
    updated_at = db.Column(db.DateTime(timezone = True), default = func.now())
    likes = db.Column(db.Integer, nullable = False)
    created_by = db.Column(db.String(36), db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    tags = db.relationship('Tag', secondary='post_tag', backref=db.backref('posts', lazy='dynamic'))

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(500), nullable = False)
    description = db.Column(db.String(500) ,nullable = False)

    posts = db.relationship('Post', backref = 'category')

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key = True, nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(300), unique = True, nullable = False)
    first_name = db.Column(db.String(300), nullable = False)
    last_name = db.Column(db.String(300))

    posts = db.relationship('Post', backref = 'author', lazy='dynamic')

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, nullable = False, primary_key = True)
    name = db.Column(db.String(500))


class PostTag(db.Model):
    __tablename__ = 'post_tag'
    post_id = db.Column(db.String(36),db.ForeignKey('posts.id'), primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key = True)