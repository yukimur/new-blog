
from flask import Flask,request,jsonify
from flask_restful import Api
from conf.mysql_conf import *
# 导入各资源类
from app.resources.user import User
from app.resources.paper import Paper
from db import db
from common import jwt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from app.models.userModel import User as userModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['JWT_SECRET_KEY'] = "yukimura"
jwt.init_app(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(User, '/user')
api.add_resource(Paper, '/paper')
api.add_resource(PaperList, '/paper')

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({"msg": "Missing username parameter"}), 400
    user = userModel.query.filter_by(username=username,password=password).first()
    if not user:
        return jsonify({"msg": "Not have this user!"}), 400
    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


if __name__ == '__main__':
    db.init_app(app)
    app.run("0.0.0.0","8007", debug=True)