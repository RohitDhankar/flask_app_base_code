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
	def load_user(user_name_from_mongo):
		print("---in --AA--user_name_from_mongo--",user_name_from_mongo)
		return user_name_from_mongo #User.query.get(user_id)

	"""
	dhankar comments  
	1/ user_id -- required from Mongo -- Not Ok to have Mongo Object ID as user_id 
	2/ why to have this method - load_user - here and also create the - main app as sen below 
	app.register_blueprint(main) -- why would main be required to use a - load_user Or a @login_manager.user_loader

	"""
	# def load_user(user_id):
	# 	return User.query.get(user_id)

	app.config.from_pyfile(config_file)
	app.register_blueprint(main)
	app.register_blueprint(auth)
	return app


	"""
	https://flask-login.readthedocs.io/en/latest/_modules/flask_login/login_manager.html#LoginManager.user_loader
	def user_loader(self, callback):
	"""