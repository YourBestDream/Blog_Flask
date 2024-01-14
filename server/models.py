from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.String(36), primary_key = True, nullable = False)
    title = db.Column(db.Text, nullable = False)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone = True), default = func.now(), nullable = False)
    updated_at = db.Column(db.DateTime(timezone = True), default = func.now())
    likes = db.Column(db.Integer, nullable = False)
    bookmarks = db.Column(db.Integer, nullable = False)
    created_by = db.Column(db.String(36), db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    # likers = db.relationship('User', secondary='likes', backref=db.backref('liked', lazy='dynamic'))
    # bookmarkers = db.relationship('User', secondary='bookmarks', backref=db.backref('bookmarked', lazy='dynamic'))
    likers = db.relationship('User', secondary='likes', back_populates='liked_posts')
    bookmarkers = db.relationship('User', secondary='bookmarks', back_populates='bookmarked_posts')

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

    # liked_posts = db.relationship('Post', secondary='likes', backref=db.backref('liked_by', lazy='dynamic'))
    # bookmarked_posts = db.relationship('Post', secondary='bookmarks', backref=db.backref('bookmarked_by', lazy='dynamic'))

    liked_posts = db.relationship('Post', secondary='likes', back_populates='likers')
    bookmarked_posts = db.relationship('Post', secondary='bookmarks', back_populates='bookmarkers')


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, nullable = False, primary_key = True)
    name = db.Column(db.String(500))


class PostTag(db.Model):
    __tablename__ = 'post_tag'
    post_id = db.Column(db.String(36),db.ForeignKey('posts.id'), primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key = True)

class Like(db.Model):
    __tablename__ = 'likes'
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), primary_key=True)
    post_id = db.Column(db.String(36), db.ForeignKey('posts.id'), primary_key=True)

class Bookmark(db.Model):
    __tablename__ = 'bookmarks'
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), primary_key=True)
    post_id = db.Column(db.String(36), db.ForeignKey('posts.id'), primary_key=True)