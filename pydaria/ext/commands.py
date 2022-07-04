import click
from ext.database import db
from ext.auth import create_user

def create_db():
    db.create_all()


def drop_db():
    db.drop_all()




def init_app(app):
    @app.before_first_request
    def cria_banco():
        db.create_all()





