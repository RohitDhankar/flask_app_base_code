

from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash , generate_password_hash
from flask_login import current_user, login_required , LoginManager , login_user, logout_user
from example_org__app.extensions import conn_mongo_atlas
from example_org__app.models import User as cls_user
from flask_bootstrap import Bootstrap


from .main import main 
from .forms import LoginForm


auth = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.login_message = u"You need to Login into the example_org_ /n auth-system to view this page ."

@auth.route('/register', methods=['GET', 'POST'])
def register():
	"""
	#curl -X POST http://127.0.0.1:5000/register -H "Content-Type: application/json" -d '{"first_name":"Test_cURL_FirstName", "last_name":"Test_cURL_LastName" , "password":"Test_cURL_password"}'
	curl -X POST http://127.0.0.1:5000/register 
	-H "Content-Type: application/json" 
	-d '{"first_name":"Test_cURL_FirstName", "last_name":"Test_cURL_LastName" , "password":"Test_cURL_password"}'
	
	"""
	if request.method == 'POST':
		mongo_atlas_client , db = conn_mongo_atlas()
		users_coll = db.users
		first_name = request.json['first_name']
		last_name = request.json['last_name']
		plain_text_password = request.json['password']
		
		print("---JSON Request through cURL - FirstName---",first_name)
		print("---JSON Request through cURL - LasttName---",last_name)
		hashed_salted_password = generate_password_hash(plain_text_password,method='pbkdf2:sha256',salt_length=8)
		print(hashed_salted_password)

		# first_name = request.form['first_name']
		# last_name = request.form['last_name']
		#plain_text_password = request.form['password']

		#hashed_salted_password = generate_password_hash(plain_text_password,method='pbkdf2:sha256',salt_length=8)
		#print(hashed_salted_password)
		#pbkdf2:sha256:150000$ylpRqlsS$edd651b01d3e828e8be4a57652a64f358d96c8ee820da0d7767cae15dd9945fa
		
		users_coll.insert({'first_name':first_name,'last_name' : last_name , 'password' :hashed_salted_password})
		#return redirect(url_for('auth.login'))
	return render_template('register.html')

"""
{"_id":{"$oid":"5fe56a53f54e35c49898fd53"},"first_name":"FirstTestName","last_name":"LastTestName","password":"pbkdf2:sha256:150000$ylpRqlsS$edd651b01d3e828e8be4a57652a64f358d96c8ee820da0d7767cae15dd9945fa"}
"""

from flask_babel import _

@auth.route('/login', methods=['GET', 'POST'])
def login():
	print("---AAA")
	form = LoginForm()
	print(form)

	if current_user.is_authenticated:
		print("---current_user---",current_user)
		form = LoginForm()
		print(form)
	else:
		#return redirect(url_for('main.index'))
		form = LoginForm()
		print(form)
	# if form.validate_on_submit():
	# 	user = User.query.filter_by(username=form.username.data).first()
	# 	if user is None or not user.check_password(form.password.data):
	# 		flash(_('Invalid username or password'))
	# 		return redirect(url_for('auth.login'))
	# 	login_user(user, remember=form.remember_me.data)
	# 	next_page = request.args.get('next')
	# 	if not next_page or url_parse(next_page).netloc != '':
	# 		next_page = url_for('main.index')
	# 	return redirect(next_page)
	#return render_template('auth/login.html', title=_('Sign In'), form=form)
	return render_template('login.html', form=form)






@auth.route('/login_1', methods=['GET', 'POST'])
def login_1():
	""" https://github.com/maxcountryman/flask-login/blob/d7b5bcf5d003274227be5c19104c59a821097cd1/flask_login/utils.py#L145
	"""
	if request.method == 'POST':
		# inputs from HTML Template Form ( if any )
		if request.form :
			first_name = request.form['first_name']
			last_name = request.form['last_name']
			plain_text_password = request.form['password']
			print("---Request HTML FORM  - FirstName---",first_name)
			print("---Request HTML FORM  - LasttName---",last_name)

		# inputs from cURL POST / JSON API end-point ( if any )
		elif request.json:
			first_name = request.json['first_name']
			last_name = request.json['last_name']
			plain_text_password = request.json['password']
			print("---JSON Request through cURL - FirstName---",first_name)
			print("---JSON Request through cURL - LasttName---",last_name)

		db = conn_mongo_atlas()
		users_coll = db.users

		query_name_from_mongo = users_coll.find({'first_name':first_name ,'last_name':last_name })
		for doc in query_name_from_mongo:
			first_name_from_mongo = doc['first_name']
			last_name_from_mongo = doc['last_name']
			plain_text_password = doc['password']
			user_name_from_mongo = first_name_from_mongo + last_name_from_mongo
			hashed_salted_password = generate_password_hash(plain_text_password,method='pbkdf2:sha256',salt_length=8)
		
		if not user_name_from_mongo :
			print("---user not found needs to Register --- ")
		if not check_password_hash(hashed_salted_password, plain_text_password):
			print("---password not found - probably needs to Register --- ")
		else:
			#print(check_password_hash(hashed_salted_password, plain_text_password)) ## return == True
			print("---user exists----",user_name_from_mongo)
			return redirect(url_for('main.questions_to_answer'))
			# user_obj = cls_user(username = user_name_from_mongo)
			# login_user(user_obj)
			# https://github.com/maxcountryman/flask-login/blob/d7b5bcf5d003274227be5c19104c59a821097cd1/flask_login/utils.py#L145
			#return redirect(url_for('main.index'))
			#return redirect(url_for('main.questions_to_answer'))
	return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('auth.login'))


### Foobar - OK code below 
# query_name_from_mongo_1 = users_coll.find( {'first_name':{'$eq':first_name} ,'last_name':{'$eq':last_name} })
# for doc1 in query_name_from_mongo_1:
# 	print("----doc1-----",doc1)

# #print("----query_name_from_mongo_1----",query_name_from_mongo_1)
# query_name_from_mongo_2 = users_coll.find({'first_name':{'$eq':first_name} ,'last_name':{'$eq':last_name} },{"first_name":1,"last_name":1,"password":1})
# print("----query_name_from_mongo_2----",query_name_from_mongo_2)
# for doc2 in query_name_from_mongo_2:
# 	print("----doc2----",doc2)
	#----doc2---- {'_id': ObjectId('5fe568c84ac3367056b28f94'), 'password': 'RandomPass#123459'}
