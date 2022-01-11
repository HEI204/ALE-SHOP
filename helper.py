import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
from datetime import datetime
import pytz
import time
import random

def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def hk_time_now():
    """ Return the current time in Hong Kong"""

    hk_timezone = pytz.timezone('Asia/Hong_Kong')
    time_now = datetime.now(hk_timezone)

    return (str(time_now.date()) + " " + str(time_now.strftime("%H:%M:%S")))

def order_id_generator():
    """ Generate order id """

    hk_timezone = pytz.timezone('Asia/Hong_Kong')
    time_now = datetime.now(hk_timezone)

    order_id = int(time.mktime(time_now.timetuple()))
    order_id += random.randint(0,10)

    return str(order_id)[0:3]+"-"+str(order_id)[3:6]+"-"+str(order_id)[6:10]