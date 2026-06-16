from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

# Cambia estos datos por los tuyos
USUARIO  = "postgres"
PASSWORD = "tu_password"
HOST     = "localhost"
PUERTO   = "5432"
BASE     = "postgres"      # nombre de tu BD en pgAdmin

DATABASE_URL = "postgresql+psycopg2://postgres:wendy123@localhost:5432/postgres"
engine = create_engine(DATABASE_URL, echo=False)

# Configurar el schema examen_bd2
def get_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    session.execute(text("SET search_path TO examen_bd2"))
    return session

Base = declarative_base()

