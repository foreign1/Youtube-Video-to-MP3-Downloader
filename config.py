import os
class Config():
    SECRET_KEY = os.urandom(24)
    FLASK_APP = 'application.py'
    FLASK_DEBUG = 1