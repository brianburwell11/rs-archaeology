from flask import Flask, render_template

from admin import admin_blueprint
from api import *
from db.db import db_blueprint


app = Flask(__name__)

app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(db_blueprint, url_prefix='/db')

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_500(e):
    return render_template('500.html'), 500
