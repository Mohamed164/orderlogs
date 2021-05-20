import gen_logs as gen
import threading
import random 

def genlogs(i): 
	if i == 60:
		gen.log_timestamp()
		i = -1 

	threading.Timer(5.0, genlogs, [i+1]).start()

	if (random.random() < 0.7):
		gen.session_existing_user()
	else:
		gen.session_new_user()



genlogs(0)
