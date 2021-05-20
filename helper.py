import time
from datetime import datetime
from datetime import timedelta
import random 
import pandas as pd
import pycountry
import string
from pathlib import Path
import pytz

def append_new_line(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

def timestamp():
    now = datetime.now(tz=pytz.utc)
    return now.strftime('%Y-%m-%dT%H:%M:%SZ')

def name():
    return random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(10));

def surname():
    return random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(6));

def birthday():
    d1 = datetime.strptime('1/1/1900 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2020 4:50 AM', '%m/%d/%Y %I:%M %p')
    return str(random_date(d1, d2).strftime('%Y-%m-%d'))

def codice_fiscale():
    return ''.join(random.choice(string.digits+ string.ascii_uppercase) for i in range(16))

def errorcode():
    return 'E' + str(random.randint(1,9))

def currency():
    currencies = ['E', 'S', 'Y', 'L', 'K', 'B']
    return random.choice(currencies)

def payment_method():
    payment_methods = ['CC', 'IBAN', 'PP', 'CRYPTO']
    return random.choice(payment_methods)

def price():
    return round(random.uniform(0.01, 999.99),2)

def countrycode():
    return random.choice(list(pycountry.countries)).alpha_2

def generate_new_username():
    new_username = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16));
    if not Path('users.csv').is_file() or new_username not in pd.read_csv('users.csv')['userid']:
        return new_username
    generate_new_username();

def language():
    return random.choice(list(pycountry.languages)).alpha_3

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    
    return start + timedelta(seconds=random_second)



