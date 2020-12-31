
import os 


SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False

""" 
Alternatively as done in the - FLASK_megaTutorial - and other such guides 
we can have a separate python module named == config.py - in which we have a class== Config 
"""