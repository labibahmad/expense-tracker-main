import yaml
import mysql.connector as mysql


import os

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, '..', 'config.yaml')

with open(config_path, 'r') as f:
    # Rest of your code

    configs = yaml.load(f, Loader=yaml.FullLoader)
    db_credintials = configs['db']
    email_sender = configs['email_sender']


# @st.cache
def get_database_connection():
    db = mysql.connect(host = db_credintials['host'],
                      user = db_credintials['user'],
                      passwd = db_credintials['passwd'],
                      database = db_credintials['database'],
                      auth_plugin= db_credintials['auth_plugin'])
    
    cursor = db.cursor()

    return cursor, db




def get_all_members(db, cursor):
	pass

def get_single_member(db, cursor):
	pass