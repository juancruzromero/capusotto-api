<h1 align="center">
  <img align="center"; src="http://petercapusotto.tv/wp-content/uploads/2016/05/logo-3.png" width="100px"; height="40px">
    CapuAPI
</h1>

_____________________________________________________________________________________
⚠️***IMPORTANTE:*** Esta API aún está en desarrollo, pero se puede hacer deploy configurando la variable DJANGO_SETTINGS_MODULE. Aún trabajando en el versionado y la organización del repositorio. Se estima hacer el deploy y poder consumir la API para el mes de agosto del 2021.
_____________________________________________________________________________________
Como fan del capocómico Peter Capusotto y el gran guionisa argentino, Pedro Saborido, hice esta API REST con información de todos los personajes de este programa de televisión y otras cositas.

La idea de este proyecto es introducir a los estudiantes a poder pensar como crear servicios API REST e ir probando cositas para aprender.

Está hecha en Python y utiliza el Framework Django.
## Ejecución:
**Deploy ubuntu:**

*Para usar sqlite3 en local:* DJANGO_SETTINGS_MODULE=config.settings.base

1) python -m venv env
2) source env/bin/activate
3) pip install -r requirements.txt
4) python manage.py makemigrations personajes
5) python manage.py migrate
6) python manage.py runserver

**Deploy con docker:**
1) docker-compose build
2) docker-compose run web python manage.py makemigrations personajes
3) docker-compose run web python manage.py migrate
4) docker-compose up
5) docker-compose down

## Anotaciones
Editar settings de producción:
En el archivo **manage.py** seteo el DJANGO_SETTINGS_MODULE para que tome los archivos de configuración.
[DJANGO_SETTINGS_MODULE](https://docs.djangoproject.com/en/3.2/topics/settings/#envvar-DJANGO_SETTINGS_MODULE)

Clave donde se crea la bd:
'NAME': BASE_DIR.**parent** / 'db.sqlite3',

