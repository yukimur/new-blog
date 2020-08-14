
from flask_restful import Resource, Api
from app.models.userModel import User as UserModel 
from flask_restful  import fields, marshal_with,reqparse,request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask import jsonify,Response

user_fields = {
    'username':   fields.String,
    'email':    fields.String,
    "role":     fields.String,
    "date_join":    fields.DateTime,
}

# parser = reqparse.RequestParser()
# parser.add_argument('username', type=str)
# parser.add_argument('password', type=str)
# parser.add_argument('email', type=str)

class User(Resource):
    @jwt_required
    @marshal_with(user_fields)
    def get(self):
        user = UserModel.query.filter_by().first()
        return user
    
    @marshal_with(user_fields)
    def post(self):
        args = request.form
        username = args.get('username', None)
        password = args.get('password', None)
        email = args.get('email', None)
        if not username or not password or not email:
            return {"msg": "Missing username parameter"}, 400
        if UserModel.query.filter_by(username=username).first():
            return {"msg": "User always res"}, 400
        # write to database
        u = UserModel(username=username,password=password,email=email)
        u.save()
        print(u,u.username)
        return u