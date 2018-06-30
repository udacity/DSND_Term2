from worldbankapp import app

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/project-one')
def project_one():
    return render_template('project_one.html')

# TODO: Add another route. You can use any names you want
# Then go into the templates folder and add an html file that matches the file name you put in the render_template method. You can create a new file by going to the + sign at the top of the workspace and clicking on Create New File. Make sure to place the new html file in the templates folder.

# TODO: Start the web app per the instructions in the instructions.md file and make sure your new html file renders correctly.