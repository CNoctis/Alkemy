import os
import logging.handlers
import sys
from datetime import datetime


class LogSystem:
    """"Class File Management proporciona métodos para manipular archivos en un directorio"""

    def __init__(self, log_name: str, set_level='DEBUG'):
        """Iniciar instancia de la clase LogSystem

        :param folder_name: Carpeta para crear un sistema de registros de ruta
        :param log_name: Registros de archivo de nombre del nombre del script
        :param set_level: Rastreo de nivel-> INFO|DEBUG|ERROR|WARNING
        """
        _folder_log = os.path.dirname(os.getcwd()) + '/logs/'
        _today = datetime.today()

        self.folder_name = _folder_log
        self.log_name = log_name
        self.set_level = set_level
        self.system_date = _today
        self.logger = self.create_instance()
        logging.info('LogSystem instance created')

    def except_handler(self, type, value, tb):
        self.logger.exception("Uncaught exception: {}".format(str(value)))

    def create_instance(self):
        td = self.system_date.strftime('%Y-%m-%d')
        log_name = f'{self.log_name}_{td}.log'
        path_file = os.path.join(self.folder_name, log_name)

        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", path_file))

        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        handler.setFormatter(formatter)

        logger = logging.getLogger()

        level = logging.getLevelName(self.set_level)
        logger.setLevel(level)
        logger.addHandler(handler)

        # Instala controlador de excepciones
        sys.excepthook = self.except_handler

        return logger
