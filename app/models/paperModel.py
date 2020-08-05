
from flask_sqlalchemy import SQLAlchemy
from conf.mysql_conf import *
from datetime import datetime
from db import db

class Paper(db.Model):
    __tablename__ = "Paper"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    summary = db.Column(db.Text)
    view = db.Column(db.Integer)
    admire = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    comments = db.relationship('Comment', backref='Paper',
                                lazy='dynamic')

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
    __tablename__ = "Comment"
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    reply = db.Column(db.Integer)
    admire = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime)
    comment_id = db.Column(db.Integer, db.ForeignKey('Comment.id'))
    paper_id = db.Column(db.Integer, db.ForeignKey('Paper.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    comments = db.relationship('Comment', backref='Comment',
                                lazy='dynamic')

    def __init__(self, comment, reply,admire):
        self.comment = comment
        self.reply = reply
        self.admire = admire
        self.upload_time = datetime.now()

    def __repr__(self):
        return '<User %r>' % self.comment