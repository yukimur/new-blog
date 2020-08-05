from flask_restful import Resource, Api
from app.models.paperModel import Paper as PaperModel,Comment as CommentModel 

class Paper(Resource):
    def get(self):
        return {'hello': 'world'}