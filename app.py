from flask import Flask
from app_config import app_config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feederDatabase.db'
app.secret_key = app_config.get('FLASK_SECRET_KEY')