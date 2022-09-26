import os
from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix = '/')
app.config.from_object(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'


if __name__ == '__main__':
    porta = int(os.environ.get('PORT', 5002))
    app.run(host = '0.0.0.0', port = porta, debug = True)