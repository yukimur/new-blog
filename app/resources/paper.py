from flask_restful import Resource, Api
from app.models.paperModel import Paper as PaperModel,Comment as CommentModel 
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

class Paper(Resource):
    def get(self):
        return {'hello': 'world'}

    @jwt_required
    def post(self):
        return {'hello': 'world'}

class PaperList(Resource):
    def get(self):
        return {'hello': 'world'}

class DateCount(Resource):
    def get(self):
        return {'hello': 'world'}

class LastestPaper(Resource):
    def get(self):
        return {'hello': 'world'}

class TagCloud(Resource):
    def get(self):
        return {'hello': 'world'}