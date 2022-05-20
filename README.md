# Challenge Data Analytics - Python

## Introduction
El presente proyecto tiene como finalidad realizar la extración de datos de un sitio web.
Los datos extraidos seran cargados en una base de datos PostgreSQL.

## Prerequisitos
- Python > 3.7.0
- PostgreSQL > 10.0.0 

## Configuración
Debera configurar las variables de .env con la información para acceder a su base de datos PostgreSQL

```
¡Importante!

.env -> Edite las credenciales de la base de datos
```

## Instalación
Para instalar las librerías necesarias para ejecutar el presente proyecto, ejecute la siguiente linea de comando.

```
pip install -r requirements.txt

o

pip install virtualenv
```
Una vez instaladas las librerias, se debe ejecutar el siguiente comando
para iniciar la instalación de la base de datos.

```
python ./scripts/deploy.py
```


## Ejecución
Para ejecutar el proyecto, se debe aplicar la siguiente comando:

```
python main.py -> Ejecución de actualización de datos
```

## Estructura del proyecto

```
|- logs -> Logs de la ejecución
|- querys -> Archivos de consultas SQL
|- storage -> Respaldo de descarga
|- scripts
|   |- deploy.py -> Script de instalación de la base de datos
|   |- download.py -> Script de descarga de datos
|   |- update_db.py -> Script de actualización de datos
|- utils -> Utilidades para el proyecto
|- .env
|- main.py
|- README.md
|- requirements.txt
```

## Autor
- [@CNoctis]

## Licencia

```
MIT License
```
