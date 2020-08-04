from flask import Flask,jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from conf.mysql_conf import *
from datetime import datetime
from user.models import User

# app = Flask(__name__)
# api = Api(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy()

class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), unique=True)
    summary = db.Column(db.Text)
    view = db.Column(db.Integer)
    admire = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    def __init__(self, title, summary,view,admire,update_time):
        self.title = title
        self.summary = summary
        self.view = view
        self.admire = admire
        self.upload_time = datetime.now()
        self.update_time = update_time

    def __repr__(self):
        return '<Paper %r>' % self.title

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    reply = db.Column(db.Integer)
    admire = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime)
    comment_id = db.Column(db.Integer, db.ForeignKey('Comment.id'))
    paper_id = db.Column(db.Integer, db.ForeignKey('Paper.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    def __init__(self, comment, reply,admire):
        self.comment = comment
        self.reply = reply
        self.admire = admire
        self.upload_time = datetime.now()

    def __repr__(self):
        return '<User %r>' % self.username