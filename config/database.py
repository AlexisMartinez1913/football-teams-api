import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Definir el archivo de la base de datos SQLite
sqlite_file_name = "../football_teams_db.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

# Crear la URL de la base de datos
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

#crear una instancia del resultado q devuelve create_engine
engine = create_engine(database_url, echo=True)

# Crear la sesión para las consultas
Session = sessionmaker(bind=engine)

# Definir la base para los modelos de SQLAlchemy
Base = declarative_base()
