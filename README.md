# CapuAPI

## Ejecución:
**Deploy ubuntu:**
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

