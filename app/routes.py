from app import app
from flask import render_template


@app.route('/')
def index():
    return 'sample'
