from flask import render_template
from app import app



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test", defaults={'name': None})
@app.route('/test/<name>')
def teste(name):
    if name:
        return "Olá, %s!" % name    
    else:
        return "Olá, usuário!"