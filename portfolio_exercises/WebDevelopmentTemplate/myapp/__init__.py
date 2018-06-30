from flask import Flask

app = Flask(__name__)

from myapp import routes
