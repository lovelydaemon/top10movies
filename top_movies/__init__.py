from flask import Flask
from flask_bootstrap import Bootstrap
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    Bootstrap(app)
    db.init_app(app)

    from .blueprints.movies.views import bp
    app.register_blueprint(bp)

    return app
