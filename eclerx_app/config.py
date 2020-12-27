import os 

class Config(object):
    ALTERNATE_SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_harcoded_secret_key_f3cfe9ed8fae309f02079dbf'