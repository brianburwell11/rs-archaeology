from os.path import join, sep

from flask import Flask, render_template, redirect
from flask_swagger_ui import get_swaggerui_blueprint

from admin import admin_blueprint
from api import *
from db.db import db_blueprint


app = Flask(__name__)

app.register_blueprint(get_swaggerui_blueprint(
                            '/api',
                            join(sep, 'static', 'swaggerui.json'),
                            config={'app_name':"RS Archaeology"}
                        ))

app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(db_blueprint, url_prefix='/db')

@app.route('/')
def index():
    return redirect('/api')
    # return render_template('index.html')

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_500(e):
    return render_template('500.html'), 500
