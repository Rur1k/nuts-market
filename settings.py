import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("DB_LOGIN")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:5432/{os.getenv("DB_NAME")} '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
