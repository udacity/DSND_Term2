from worldbankapp import app

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/project-one')
def project_one():
    return render_template('project_one.html')

# new route
@app.route('/new-route')
def new_route():
    return render_template('new_route.html')