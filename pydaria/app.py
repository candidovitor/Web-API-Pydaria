from flask import Flask
from ext import configuration
from ext import admin
from ext import auth
from ext import appearance
from ext import database
from blueprints import views

app = Flask(__name__)

configuration.init_app(app)
admin.init_app(app)
appearance.init_app(app)
auth.init_app(app)
database.init_app(app)
views.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)