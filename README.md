# CapuAPI

**Comandos:**

docker-compose up

docker-compose run web python manage.py makemigrations

Editar settings de producción:

En el archivo **manage.py** seteo el DJANGO_SETTINGS_MODULE para que tome los archivos de configuración.

[DJANGO_SETTINGS_MODULE](https://docs.djangoproject.com/en/3.2/topics/settings/#envvar-DJANGO_SETTINGS_MODULE)

python manage.py makemigrations personajes

Clave donde se crea la bd
'NAME': BASE_DIR.parent / 'db.sqlite3',

Deploy:
1) docker-compose build
2) docker-compose run web python manage.py makemigrations personajes
3) docker-compose run web python manage.py migrate
4) docker-compose up
4) docker-compose down
