<h1 align="center">
    <img src="https://d3b5jqy5xuub7g.cloudfront.net/wp-content/uploads/2019/05/PeterCapusottoYSusVideos.jpg" alt="Capusotto" align="center" width="80px">
    <br>
    Capusotto API
</h1>

## Descripción del proyecto
API de los personajes de Peter Capusotto📺. Escrita en Python, aplicando buenas prácticas y coso.

- Desarrollado con Python 3.13.3.

## Diagrama de diseño

![imagen](./docs/diagram.svg)

## Cómo correr el proyecto

```bash
git clone https://github.com/tu_usuario/capusotto_api.git
cd capusotto_api
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
### Con Docker:

```bash
git clone https://github.com/tu_usuario/capusotto_api.git
cd capusotto_api
docker build -t capusotto_api .
docker run -d -p 8000:8000 capusotto_api
```

## Features principales
- Listar personajes
- Obtener detalles de un personaje

**Mejoras cuando se defina base de datos:**
- Agregar nuevos personajes 
- Actualizar personajes existentes
- Eliminar personajes

## Próximos features:
- Integración con base de datos PostgreSQL.
- Mejorar ADD, UPDATE y DELETE de personajes.
- Mejorar 404 en frontend.