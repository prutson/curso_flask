from flask import render_template
from app import app


@app.route("/index/<user>")
@app.route("/", defaults={'user':None})
def index(user):
    return render_template('index.html', 
                           user=user)

@app.route("/test", defaults={'name': None})
@app.route('/test/<name>')
def teste(name):
    if name:
        return "Olá, %s!" % name    
    else:
        return "Olá, usuário!"