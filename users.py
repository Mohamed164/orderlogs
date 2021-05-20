import pandas as pd
import random
import string
import helper as h
from pathlib import Path

users_file = Path('users.csv')
logs_file = Path('logs.log')

def sign_up_user(name, surname, codice_fiscale, birthday, language):
	# check if file exits 
	if not users_file.is_file():
		h.append_new_line(users_file, 'userid,name,surname,cf,birthday,language')
		
	new_user = h.generate_new_username() +','+ name +','+ surname +','+ codice_fiscale +','+ birthday +','+language
	h.append_new_line(users_file, new_user)

	new_user_log = 'user:'+ h.generate_new_username() +', userName:'+ name +', userSurname:'+ surname +', user_CF:'+ codice_fiscale +', birthday:'+ birthday +', language:'+language
	h.append_new_line(logs_file, str(h.timestamp()) + ' [DEBUG] - New user - '+new_user_log)

def is_signed_up(userid):
	df = pd.read_csv('users.csv')
	return userid in df['userid']

def sign_in_user(userid, storecode):
	h.append_new_line(logs_file, str(h.timestamp()) + ' [DEBUG] - User login - '+'user:'+ userid + ', store:' + storecode)

def log_out_user(userid, storecode):
	h.append_new_line(logs_file, str(h.timestamp()) + ' [DEBUG] - User logout - '+'user:'+ userid + ', store:' + storecode)
	
def get_random_userid():
	df = pd.read_csv('users.csv')
	return random.choice(list(df['userid']))
