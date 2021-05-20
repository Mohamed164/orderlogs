import helper as h
from pathlib import Path
import pandas as pd
import random
import string
import errors as e

file_stores = Path("stores.csv")
file_products = Path("products.csv")
file_logs = Path('logs.log')


def gen_stores(num_of_stores):
	# generate random stores 
	if not file_stores.is_file():
		h.append_new_line(file_stores, 'storecode,last_order_num')

	for i in range(num_of_stores):
		new_store = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(3));
		h.append_new_line(file_stores, new_store + ',' + '0'*10)
	

def gen_products_for_stores():
	if not file_products.is_file():
		h.append_new_line(file_products, 'productid,storecode,price,currency')

	storecodes = pd.read_csv(file_stores)['storecode']
	productids = pd.read_csv(file_products) 

	ids = [i + str(j) for i in ['A','V','E','C','I'] for j in range(1,6)]
	for storecode in storecodes:
		curr = h.currency()
		# todo: an iterator!
		for productid in ids:
			h.append_new_line(file_products, productid + ','+ storecode +','+ str(h.price())+','+ curr)

def next_product_id_for_store(storecode):
	if not file_stores.is_file():
		raise Exception('store.csv file doesn\'t exist')

	df = pd.read_csv(file_stores)
	current_id = df[df['storecode'] == storecode].iloc[0]['last_order_num']
	df.loc[df['storecode'] == storecode,'last_order_num'] = current_id +1
	df.to_csv(file_stores, index=False)
	return current_id +1

def order(userid, storecode, productids):
	order_id = str(next_product_id_for_store(storecode))
	err = random_error(order_id, storecode)
	if not err:
		h.append_new_line(file_logs, str(h.timestamp()) + ' [INFO] - New order - ' + 'user:'+userid +', products:'+productids +', store:'+storecode+', country:'+h.countrycode()+', totPrice:'+str(h.price())+h.currency()+', paymentMethod:'+h.payment_method()+', orderId:'+order_id)


def get_random_storecode():
	df = pd.read_csv('stores.csv')
	return random.choice(list(df['storecode']))

	
def get_random_productids():
	ids = [i + str(j) for i in ['A','V','E','C','I'] for j in range(1,6)]
	return ','.join([random.choice(ids) for _ in range(random.randint(1,4))])

def random_error(orderid, storecode):
	throw_error = random.random() > 0.8
	if (throw_error):
		e.log_error(orderid, storecode)
	return throw_error