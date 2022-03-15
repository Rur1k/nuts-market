from flask import render_template
from settings import app


@app.route('/')
def index():
    return 'Hello, World!'
