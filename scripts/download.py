import os
import locale
import logging
import requests
import sys
sys.path.insert(0, os.path.dirname(os.getcwd()))
from bs4 import BeautifulSoup
from datetime import datetime
from utils.log_system import LogSystem

LogSystem('download')
locale.setlocale(locale.LC_TIME, '')

# Link a consultar
LINKS_CONSULTAR = {
    'museos': 'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d',
    'salas_cine': 'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae',
    'bibliotecas': 'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7'
}

# Ruta de trabajo y tiempo
td = datetime.today()
root_dir = os.path.dirname(os.getcwd())


def download_file(link_download, categoria):

    req_download = requests.get(link_download)
    # Comprobamos que la petición nos devuelve un Status Code = 200
    status_code = req_download.status_code
    
    # Direccionamiento
    folder = os.path.join(root_dir, 'storage', categoria, td.strftime('%Y-%B'))
    # Nombre del archivo en formato categoría\año-mes\categoria-dia-mes-año.csv
    name_file = f"{categoria}-{td.strftime('%d-%m-%Y')}.csv"

    if not os.path.exists(folder):
        os.makedirs(folder)
    
    full_path = f"{folder}/{name_file}"

    if status_code == 200: # las web tienes status de respuesta por cada peticion http
        # guardamos el archivo
        with open(full_path, 'wb') as file:
            file.write(req_download.content)
            logging.info(f"Archivo descargado: {full_path}")
    else:
        logging.warning(f"Error {status_code} al descargar {categoria}")


def scrapping():
    """
    Scrapping de los datos de links a consultar
    """

    for categoria, link in LINKS_CONSULTAR.items():
        req = requests.get(link)
        # Comprobamos que la petición nos devuelve un Status Code = 200
        status_code = req.status_code
        if status_code == 200:
            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            html = BeautifulSoup(req.text, "html.parser")

            # Buscamos el elemento: class="col-md-2 col-xs-12 resource-actions"
            buttons = html.find_all('a', class_='btn btn-green btn-block')
            link_download = buttons[0].get('href')
            download_file(link_download, categoria)
        else:
            logging.warning(f"Error al abrir web Error:{status_code}, consultar: {categoria}")
            print("Status Code %d" % status_code)


def main():
    try:
        scrapping()
        logging.info("Proceso finalizado")
    except Exception as e:
        logging.error(f"Error en la descarga: {e}")


if __name__ == '__main__':
    main()
