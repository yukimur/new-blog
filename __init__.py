
from flask import Flask

def create_app(config_filename):
    from . import user, paper
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    user.init_app(app)
    paper.init_app(app)
    return app