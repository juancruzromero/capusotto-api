<h1 align="center">
    <img src="https://d3b5jqy5xuub7g.cloudfront.net/wp-content/uploads/2019/05/PeterCapusottoYSusVideos.jpg" alt="Capusotto" align="center" width="80px">
    <br>
    Capusotto API - Arquitectura
</h1>

## Descripción del proyecto
API de los personajes de Peter Capusotto📺. Escrita en Python, aplicando buenas prácticas y coso.

## Stack

### Frontend
- **HTML5** - Estructura básica
- **JavaScript** - Básico para interactividad
- **Tailwind CSS** - Framework CSS para estilos

### Backend
#### Primera etapa:
- **Python** - Lenguaje principal
- **FastAPI** - Framework web
- **Docker** - Contenedor para desarrollo y despliegue
#### Segunda etapa:
- **PostgreSQL** - Base de datos relacional
- **SQLAlchemy** - ORM para interacción con la base de datos
- **Alembic** - Herramienta de migraciones de base de datos
- **unittest** - Framework de pruebas unitarias

## Arquitectura del sistema

Frontend simple para consumir la API RESTful.

Monolito modular con separación clara entre capas:
- **Capa de presentación**: Maneja las solicitudes HTTP y respuestas.
- **Capa de negocio**: Contiene la lógica de la aplicación.
- **Capa de datos**: Interactúa con la base de datos.

## Entidades

### Personaje
Representa un personaje de Capusotto con atributos como nombre, descripción, y episodios asociados.

- id
- nombre
- descripción
- frase
- video

## Contratos

### Personaje JSON ejemplo
```json
{
  "id": 1,
  "nombre": "Luis Almirante Brown",
  "descripcion": "Un rockero de izquierda que vive en una eterna revolución mental.",
  "frase": "El rock es peronista",
  "video": "https://www.youtube.com/watch?v=BWdvx5RhwoI"
}
```

## Endpoints
- `GET /characters`: Lista todos los personajes.
- `GET /characters/{id}`: Obtiene un personaje por ID.
- `POST /characters`: Crea un nuevo personaje.
- `PUT /characters/{id}`: Actualiza un personaje existente.
- `DELETE /characters/{id}`: Elimina un personaje.

## Comentarios finales
El enfoque es mantener la simplicidad y funcionalidad core sin features adiciones complejas.