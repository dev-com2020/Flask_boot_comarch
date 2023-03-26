from flask import render_template, request

from app import app

@app.route('/')
def homepage():
    name = request.args.get('name')
    number = request.args.get('number')
    # if not name:
    #     name = 'nieznany'
    return render_template('index2.html', name=name, number=number)
