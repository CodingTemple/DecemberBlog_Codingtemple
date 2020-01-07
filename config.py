import os
basedir = os.path.abspath(os.path.dirname(__file__)) 
# Tell python to look at all files the same on ANY OS (Windows/Mac/Linux)

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'