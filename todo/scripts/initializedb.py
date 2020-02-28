import os

from sqlalchemy import engine_from_config

from todo import SQL_URL
from todo.models import Base

def main():
    settings = {'sqlalchemy.url': SQL_URL}
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    if bool(os.environ.get('DEBUG', '')):
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)