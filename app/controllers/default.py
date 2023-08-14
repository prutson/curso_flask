from flask import render_template
from app import app
import datetime
from app.models.forms import LoginForm


@app.route("/")
def index():
    return render_template('index.html', 
                           current_time=datetime.datetime.now().year)


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', 
                           current_time=datetime.datetime.now().year,
                           form=form)


@app.route("/test", defaults={'name': None})
@app.route('/test/<name>')
def teste(name):
    if name:
        return "Olá, %s!" % name    
    else:
        return "Olá, usuário!"