import os
import sys
import logging
sys.path.insert(0, os.path.dirname(os.getcwd()))
from utils.db import get_db_engine, read_query
from utils.log_system import LogSystem

LogSystem('deploy')
root = os.path.dirname(os.getcwd())

def main():
    """
    Creación de base de datos y tablas
    """
    conn = get_db_engine().connect()
    sql = read_query(f'{root}/querys/install.sql')
    print('Deploying...')
    conn.execute(sql)
    conn.close()
    logging.info('Deployed')



if __name__ == '__main__':
    try:
        main()
        logging.info('Proceso finalizado')
    except Exception as e:
        logging.error(e)
