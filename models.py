from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nuts_admin:admin@127.0.0.1:5432/nuts_market_db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
