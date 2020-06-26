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


@app.route('/application', methods=['POST', 'GET', 'DELETE'])
def apps():
    companies = Application.query.all()
    if request.method == "POST":
        company = request.form.get("company")
        role = request.form.get("role")
        app_id = request.form.get("app_id")
        if (role is not None) and (company is not None):
            new_app = Application(company=company, role=role)
            db_session.add(new_app)
            db_session.commit()
        elif app_id is not None:
            print(app_id)
            to_be_deleted = Application.query.filter_by(id=app_id).first()
            db_session.delete(to_be_deleted)
            db_session.commit()
    companies = Application.query.all()
    return render_template("applications.html", apps=companies)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
