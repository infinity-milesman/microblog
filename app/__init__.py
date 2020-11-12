from flask import Flask

from config import Config

app =Flask(__name__)

app.config.from_object(Config)
# def create_app():
#     app =Flask(__name__)
#     return app
# from flask_debugtoolbar import DebugToolbarExtension

# toolbar = DebugToolbarExtension(app)
from app import routes
from .api.views import api
app.register_blueprint(api)