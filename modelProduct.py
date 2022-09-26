from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)
db = MySQL(app)
