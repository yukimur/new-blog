
from flask import Flask
from flask_restful import Api
from conf.mysql_conf import *
# 导入各资源类
from app.resources.user import User
from app.resources.paper import Paper
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(User, '/user/<string:name>')
# api.add_resource(UserList, '/users')
# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    db.init_app(app)
    app.run("0.0.0.0","8007", debug=True)