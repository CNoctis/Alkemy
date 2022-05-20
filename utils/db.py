from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os
from dotenv import load_dotenv

load_dotenv()
server = os.getenv('PSQL_SERVER')
database = os.getenv('PSQL_DATABASE')
username = os.getenv('PSQL_USERNAME')
password = os.getenv('PSQL_PASSWORD')


def get_db_engine() -> create_engine:
    """
    Returns a SQLAlchemy engine for the database.
    :return: SQLAlchemy engine
    """
    return create_engine(f'postgresql://{username}:{password}@{server}/{database}')


def read_query(path: str) -> str:
    """
    Lee una consulta de un archivo y la devuelve como una cadena.
    :param path: Ruta al archivo
    :return: consulta como un string
    """
    query = open(path, 'rb').read().decode('utf-8')
    # Remueve las lineas de comentario
    query = query.split('\n')
    query = [q for q in query if not q.startswith('--')]
    query = text('\n'.join(query))

    return query
