
from conf.mysql_conf import *
from datetime import datetime
from db import db

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
    role = db.Column(db.String(32))
    date_join = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    papers = db.relationship('Paper', backref='User',
                                lazy='dynamic')
    comments = db.relationship('Comment', backref='User',
                            lazy='dynamic')
    def __init__(self, username, email,password,role,last_login):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.date_join = datetime.now()
        self.last_login = last_login

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == "__main__":
    db.create_all()