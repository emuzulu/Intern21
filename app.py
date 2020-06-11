from flask import Flask, render_template, request
from database import init_db
from database import db_session
from models import Application
from crypt import encrypt


init_db()




app = Flask(__name__)
app.config['DEBUG'] = False


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/application', method=['POST', 'GET'])
def apps():
    error = None
    companies = Application.query.all()
    if request.form == "POST":
        print(request.form['id'])
    else:
        error = "Invalid action"
    return render_template("applications.html", error=error, apps=companies)



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()