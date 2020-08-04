from flask import Flask,jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os
import json
from flask_swagger import swagger
from conf.mysql_conf import *
from user.models import User

app = Flask(__name__)
api = Api(app)



class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run("0.0.0.0","8007",debug=True)