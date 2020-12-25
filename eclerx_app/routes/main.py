from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required , LoginManager
from werkzeug.utils import secure_filename
import pandas as pd

from eclerx_app.extensions import conn_mongo_atlas

main = Blueprint('main', __name__)

@main.route('/main_index')
def index():
	mongo_atlas_client , db = conn_mongo_atlas()
	print(mongo_atlas_client)
	users_coll = db.test_users_1
	print("---users_coll----",users_coll)
	users_coll.insert({'USER_NAME':'Test_User_1'})
	print("---Inserted user ---")
	#return render_template('index.html', **context)
	return render_template('index.html')


@main.route('/questionnaire',methods=['GET','POST'])
def questionnaire():
	if request.method == 'POST':
		mongo_atlas_client , db = conn_mongo_atlas()
		#print(mongo_atlas_client)
		users_coll = db.questions
		print("---users_coll----",users_coll)
		df = pd.read_csv(request.files.get('file'))
		print(df)
	return render_template('admin_upload.html')


@main.route('/admin_upload_q',methods=['GET','POST'])
def admin_upload_q():
	if request.method == 'POST':
		mongo_atlas_client , db = conn_mongo_atlas()
		#print(mongo_atlas_client)
		users_coll = db.questions
		print("---users_coll----",users_coll)
		df = pd.read_csv(request.files.get('file'))
		print(df)
	return render_template('admin_upload.html')#, shape=df.shape)
