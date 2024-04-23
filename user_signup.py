from flask import Flask, url_for,session , redirect, render_template, abort
from authlib.integrations.flask_client import OAuth
import json, requests
from app_config import app_config
from app import app

oauth = OAuth(app)
oauth.register(
    'my_flask_app',# this is the name of the app used in the login route /google-login
    client_id=app_config.get('OAUTH2_CLIENT_ID'),
    client_secret=app_config.get('OAUTH2_CLIENT_SECRET'),
    server_metadata_url = app_config.get('OAUTH2_META_URL'),
    # got the scopes from -> https://developers.google.com/identity/protocols/oauth2/scopes
    client_kwargs={
        'scope':'openid profile email  https://www.googleapis.com/auth/user.birthday.read https://www.googleapis.com/auth/user.gender.read '
    }
    )