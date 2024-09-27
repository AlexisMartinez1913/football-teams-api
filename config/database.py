import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../football_teams_db.sqlite"

base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

#crear una instancia del resultado q devuelve create_engine
engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
