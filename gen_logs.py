import helper as h 
import users as u
import stores as s 
import random 
import errors as e
from pathlib import Path

logs_file = Path('logs.log')

def session_existing_user():
	userid = u.get_random_userid()
	_session(userid)

def session_new_user():
	new_user_id = h.generate_new_username()
	u.sign_up_user(h.name(), h.surname(), h.codice_fiscale(), h.birthday(), h.language())
	_session(new_user_id)

def _session(userid):
	storecode = s.get_random_storecode()
	#sign in 
	u.sign_in_user(userid, storecode)
	#order
	for i in range(random.randint(1,4)):
		productids = s.get_random_productids()
		s.order(userid, storecode, productids)
	#log_out
	u.log_out_user(userid, storecode)

def log_timestamp():
	h.append_new_line(logs_file,  '### '+str(h.timestamp())+' ###')
