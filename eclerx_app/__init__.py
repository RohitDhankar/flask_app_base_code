from flask import Flask 
from .routes.main import main 
from .routes.auth import auth 

def create_app(config_file='settings.py'):
	app = Flask(__name__)
	app.config.from_pyfile(config_file)
	app.register_blueprint(main)
	app.register_blueprint(auth)
	return app