import helper as h
from pathlib import Path

file_logs = Path('logs.log')

def log_error(orderid, storecode):
	h.append_new_line(file_logs, str(h.timestamp()) + ' [ERROR] - Error Occurred - ' +'store:'+ storecode+ ', orderId:'+orderid+', errorCode:'+h.errorcode())