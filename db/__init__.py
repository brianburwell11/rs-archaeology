"""Objects, functions, and constants used to maintain and read from a local Database."""

from os.path import abspath, dirname, join

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .models import *

DB_NAME = 'rs_archaeology'
DB_URL = f"sqlite:///{join(dirname(abspath(__file__)), f'{DB_NAME}.db')}"

engine = create_engine(DB_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


__all__ = [
    'DB_NAME',
    'DB_URL',
    'Session',
    'TABLE_NAMES',
    'TABLES',
    'Material',
    'Artefact',
    'Collector',
    'Collection',
    'Reward',
    'Mystery'
]
