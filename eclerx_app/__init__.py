from flask import Flask 
from .models import User
from .extensions import login_manager

from .routes.main import main 
from .routes.auth import auth 

def create_app(config_file='settings.py'):
	app = Flask(__name__)
	login_manager.init_app(app)
	login_manager.login_view = 'auth.login'
	
	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(user_id)

	app.config.from_pyfile(config_file)
	app.register_blueprint(main)
	app.register_blueprint(auth)
	return app


	"""
	https://flask-login.readthedocs.io/en/latest/_modules/flask_login/login_manager.html#LoginManager.user_loader
	def user_loader(self, callback):
	"""