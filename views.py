from flask import (Flask, Blueprint, render_template)

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template('base.html')