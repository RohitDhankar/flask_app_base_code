
from werkzeug.security import generate_password_hash

from flask_login import LoginManager , UserMixin
from flask_login import current_user, login_user, logout_user, login_required
from .extensions import conn_mongo_atlas
#https://flask-login.readthedocs.io/en/latest/#login-example


from flask_login import UserMixin

class User(UserMixin):
	def __init__(self, username, email=None, password=None, _id=None):
		self.username = username
		self.email = email
		self.password = password
		self._id = _id
		#self._id = uuid.uuid4().hex if _id is None else _id

	def is_authenticated(self):
		return True
	def is_active(self):
		return True
	def is_anonymous(self):
		""" by default return == False , for an Authenticated user 
			we dont want anonymous users 
		"""    
		return False

	def get_id(self):
		return self._id

	@classmethod
	def user_cls_username(cls, username):
		mongo_atlas_client , db = conn_mongo_atlas()
		users_coll = db.users

		query_name_from_mongo = users_coll.find({'first_name':first_name ,'last_name':last_name })
		for doc in query_name_from_mongo:
			first_name_from_mongo = doc['first_name']
			last_name_from_mongo = doc['last_name']
			plain_text_password = doc['password']
			user_name_from_mongo = first_name_from_mongo + last_name_from_mongo

		data = Database.find_one("users", {"username": username})
		if data is not None:
			return cls(**data)

	@classmethod
	def user_cls_email(cls, email):
		data = Database.find_one("users", {"email": email})
		if data is not None:
			return cls(**data)

	@classmethod
	def user_cls_id(cls, _id):
		data = Database.find_one("users", {"_id": _id})
		if data is not None:
			return cls(**data)

	@staticmethod
	def login_valid(email, password):
		verify_user = User.get_by_email(email)
		if verify_user is not None:
			return bcrypt.check_password_hash(verify_user.password, password)
		return False

	@classmethod
	def register(cls, username, email, password):
		user = cls.get_by_email(email)
		if user is None:
			new_user = cls( username, email, password)
			new_user.save_to_mongo()
			session['email'] = email
			return True
		else:
			return False

	def json(self):
		return {
			"username": self.username,
			"email": self.email,
			"_id": self._id,
			"password": self.password
		}

	def save_to_mongo(self):
		Database.insert("users", self.json())







