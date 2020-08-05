
from flask_restful import Resource, Api
from app.models.userModel import User as UserModel 

class User(Resource):
    def get(self):
        return {'hello': 'world'}