Checklist de mi colección
=========================

Descripción
-----------
Este repositorio contiene una aplicación que tiene dos funcionalidades importantes.

En la primera funcionalidad tenemos un scrap que obtiene información de un post de la página [https://coleccionablesblog.com.ar](https://coleccionablesblog.com.ar/).
La data es almacenada en una base de datos [SQLite](https://www.sqlite.org/).

La segunda funcionalidad expone la información almacenada en un template simple con la opción de seleccionar o marcar.
Esta parte esta desarrollada utilizando [Flask](https://flask.palletsprojects.com/en/2.0.x/)

El objetivo de la aplicación es tener un pequeño checklist o control de seguimiento.
En este caso en particular estamos tomando como ejemplo [**"La colección definitiva de novelas gráficas de Marvel"**](https://es.wikipedia.org/wiki/La_colecci%C3%B3n_definitiva_de_novelas_gr%C3%A1ficas_de_Marvel)


Pre-requisitos
--------------
Se recomienda el uso de [Python 3.9](https://www.python.org/downloads/)

Requerimientos
--------------
Se necesita instalar los siguientas librerías:

1. beautifulsoup4==4.9.3  
   `sudo pip install beautifulsoup4`
2. lxml==4.6.3  
   `sudo pip install lxml`
3. Flask==2.0.1  
   `sudo pip install Flask`
4. Flask-SQLAlchemy==2.5.1  
   `sudo pip install Flask-SQLAlchemy`
5. python-dotenv==0.17.1  
   `sudo pip install python-dotenv`

Inicio
------

1. clonar el repositorio:
  `git clone git@github.com:jack-factor/my-mv-collection-py.git`
2. Entorno virtual  
  `virtualenv -p python3.9 venv`  
  `source venv/bin/activate`
3. Instalar requerimientos:
  `pip install -r requirements.txt`  
4. Ejcutar:
  `python run.py`  
5. Para ejecutar el scrap. Abri el siguiente enlace [http://127.0.0.1:5010/scrap](http://127.0.0.1:5010/scrap).
   Esto ejecturá el scrap, creará la base de datos y almacenará la información
6. Para ver la aplicación web debemos ir al index de la aplicación [http://127.0.0.1:5010](http://127.0.0.1:5010/).