from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required , LoginManager
from werkzeug.utils import secure_filename
import pandas as pd

from example_org__app.extensions import conn_mongo_atlas

main = Blueprint('main', __name__)

@main.route('/main_index')
def index():
	db = conn_mongo_atlas()

	users_coll = db.test_users_1
	print("---users_coll----",users_coll)
	#users_coll.insert({'USER_NAME':'Test_User_1'})
	print("---Inserted user ---")
	#return render_template('index.html', **context)
	return render_template('index.html')


@main.route('/questionnaire',methods=['GET','POST'])
def questionnaire():
	if request.method == 'POST':
		db = conn_mongo_atlas()
		#print(mongo_atlas_client)
		users_coll = db.questions
		print("---users_coll----",users_coll)
		df = pd.read_csv(request.files.get('file'))
		print(df)
	return render_template('admin_upload.html')


@main.route('/admin_upload_q',methods=['GET','POST'])
def admin_upload_q():
	if request.method == 'POST':
		db = conn_mongo_atlas()
		#print(mongo_atlas_client)
		users_coll = db.questions
		print("---users_coll----",users_coll)
		df = pd.read_csv(request.files.get('file'))
		print(df)
	return render_template('admin_upload.html')#, shape=df.shape)


#@login_required
@main.route('/questions_to_answer')
def questions_to_answer():
	# if current_user.candidate_type:
	# 	return redirect(url_for('main.index_for_candidate_type'))
	db = conn_mongo_atlas()
	questions_coll = db.questions
	query = {}
	questions_cursor = questions_coll.find(query)
	df_q_all = pd.DataFrame(list(questions_cursor))
	del df_q_all['_id']
	ls_q_all = df_q_all['QUESTIONS'].tolist()

	# data = json.loads(df_q_all.to_json(orient='split'))
	# dict_json = {}
	# dict_json['data_json'] = data

	context = {
		'dict_q_all' : df_q_all.to_dict(orient='split')
	}
	# context = {
	# 	'df_html' : df_html
	# }

	return render_template('questions_to_answer.html', ls_q_all = df_q_all['QUESTIONS'].tolist())
	#/example_org__app/templates/questions_to_answer.html
