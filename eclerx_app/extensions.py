

from flask_login import LoginManager
import pymongo
import urllib

login_manager = LoginManager()
print("--exten--login_manager----",login_manager)

def conn_mongo_atlas():
	conn_str = "mongodb://example_org__admin:" + urllib.parse.quote("some_pass73") + "@example_org_-shard-00-00.2tddk.mongodb.net:27017,example_org_-shard-00-01.2tddk.mongodb.net:27017,example_org_-shard-00-02.2tddk.mongodb.net:27017/db_test?ssl=true&replicaSet=atlas-nf69f3-shard-0&authSource=admin&retryWrites=true&w=majority"
	mongo_atlas_client = pymongo.MongoClient(conn_str)
	#print("---mongo_atlas_client-----",mongo_atlas_client)
	db = mongo_atlas_client.example_org_
	return db

# client = pymongo.MongoClient("mongodb://example_org__admin:<password>@example_org_-shard-00-00.2tddk.mongodb.net:27017,example_org_-shard-00-01.2tddk.mongodb.net:27017,example_org_-shard-00-02.2tddk.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-nf69f3-shard-0&authSource=admin&retryWrites=true&w=majority")
# db = client.test
# Not used -- #https://flask-pymongo.readthedocs.io/en/latest/

"""
$ python -c "import ssl; print(getattr(ssl, 'HAS_SNI', False))"
True
"""

"""
(MongoClient(host=['example_org_-shard-00-01.2tddk.mongodb.net:27017', 'example_org_-shard-00-02.2tddk.mongodb.net:27017', 'example_org_-shard-00-00.2tddk.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, ssl=True, replicaset='atlas-nf69f3-shard-0', authsource='admin', retrywrites=True, w='majority'), Database(MongoClient(host=['example_org_-shard-00-01.2tddk.mongodb.net:27017', 'example_org_-shard-00-02.2tddk.mongodb.net:27017', 'example_org_-shard-00-00.2tddk.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, ssl=True, replicaset='atlas-nf69f3-shard-0', authsource='admin', retrywrites=True, w='majority'), 'test'))
"""

"""
mongoimport --uri mongodb+srv://example_org__admin:some_pass73@example_org_.2tddk.mongodb.net/db_test --collection users --type csv --file test_users.csv
"""


