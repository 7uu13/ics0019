from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

DB_URL = 'sqlite:///kohvikud.db'

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
app.secret_key="tere"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
