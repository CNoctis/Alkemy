import os
import locale
import logging
import pandas as pd
import sys
sys.path.insert(0, os.path.dirname(os.getcwd()))
from datetime import datetime
from utils.db import get_db_engine, read_query
from utils.log_system import LogSystem

LogSystem('update_db')

locale.setlocale(locale.LC_TIME, '')
root_dir = os.path.dirname(os.getcwd())

td = datetime.today()

file = f"{root_dir}/storage/%s/{td.strftime('%Y-%B')}/%s-{td.strftime('%d-%m-%Y')}.csv"

FILES = [
    'bibliotecas', file % ('bibliotecas', 'bibliotecas'),
    'museos', file % ('museos', 'museos'),
    'salas_cine', file % ('salas_cine', 'salas_cine'),
]

DB_COLS = [
    'cod_localidad', 'id_provincia', 'id_departamento', 'categoria', 'provincia', 'localidad', 'nombre',
    'domicilio', 'cod_postal', 'telefono', 'mail', 'web', 'fuente', 'pantallas','butacas','espacio_incaa', 'fecha_carga'
]
DF_COLS = ['cod_loc', 'idprovincia', 'iddepartamento', 'categoria', 'provincia', 'localidad', 'nombre', 'domicilio',
           'cp', 'telefono', 'mail', 'web', 'fuente', 'pantallas', 'butacas', 'espacio_incaa']

def normalize_df(df):
    # Remueve acentos y caracteres especiales
    df.columns = df.columns.str.normalize('NFKD')
    df.columns = df.columns.str.encode('ascii', errors='ignore')
    df.columns = df.columns.str.decode('utf-8')
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace('direccion', 'domicilio')
    return df


def filter_df(df, cols):
    # Crea columnas si no existen
    for col in cols:
        if col not in df.columns:
            df[col] = None
    # Filtro de columnas
    df = df[cols]

    return df


def delete_data():
    conn = get_db_engine().connect()
    conn.execute("DELETE FROM espacios_culturales where fecha_carga = '{}'".format(td.strftime('%Y-%m-%d')))
    conn.execute(
        "DELETE FROM estadistica_culturales_categoria where fecha_carga = '{}'".format(td.strftime('%Y-%m-%d')))
    conn.execute("DELETE FROM estadistica_culturales_fuente where fecha_carga = '{}'".format(td.strftime('%Y-%m-%d')))
    conn.execute("DELETE FROM estadistica_cines where fecha_carga = '{}'".format(td.strftime('%Y-%m-%d')))
    conn.execute(
        "DELETE FROM estadistica_culturales_provincia where fecha_carga = '{}'".format(td.strftime('%Y-%m-%d')))


def generate_statics():
    engine = get_db_engine()
    conn = engine.connect()

    # Lee query para generar_estadistica
    query = read_query(f'{root_dir}/querys/generar_estadistica.sql')
    conn.execute(query, {'fecha_carga': td.strftime('%Y-%m-%d')})



def main():
    # filtra archivos si no existen
    filter_files = [f for f in FILES if os.path.exists(f)]
    logging.info(f'Archivos a procesar: {filter_files}')

    if len(filter_files) > 0:
        # Crea un dataframe apartir del archivo csv
        filter_files = [normalize_df(pd.read_csv(f)) for f in filter_files]
        df_filter = [filter_df(f, DF_COLS) for f in filter_files]

        df = pd.concat(df_filter, ignore_index=True)

        # Añade columna con fecha_carga
        df['fecha_carga'] = td.strftime('%Y-%m-%d')

        # Elimina datos
        logging.info('Eliminando datos')
        delete_data()

        # Inserta datos a la base de datos
        engine = get_db_engine()

        logging.info(f'Cantidad de registros a cargar: {len(df)}')
        df.rename(columns=dict(zip(df.columns, DB_COLS))).to_sql(name="espacios_culturales",
                                                                 con=engine,
                                                                 if_exists="append",
                                                                 index=False,
                                                                 index_label=None)
        # Genera estadistica
        logging.info('Generando estadisticas')
        generate_statics()
    else:
        logging.info('No hay archivos para procesar')

if __name__ == '__main__':
    try:
        main()
        logging.info('Proceso finalizado')
    except Exception as e:
        logging.error(e)
