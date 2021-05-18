from flask import Flask


def create_app(settings):
    app = Flask(__name__)
    app.config.from_object(settings)
    
    from api.controller import app_blueprint
    app.register_blueprint(app_blueprint)

    return app

