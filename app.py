from flask import Flask, render_template

from admin import admin_blueprint
from api import api_blueprint

app = Flask(__name__)

app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(api_blueprint, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view_artefacts():
    return render_template('view-artefacts.html')

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_500(e):
    return render_template('500.html'), 500
