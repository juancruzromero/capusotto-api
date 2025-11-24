""" Archivo main.py que define la API de FastAPI para
gestionar personajes de Peter Capusotto.  Incluye las rutas.
"""
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from typing import List

from models import Character, CharacterCreate, CharacterUpdate
import service

BASE_DIR = Path(__file__).parent
app = FastAPI(
    title="Capusotto API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# FRONTEND:
# El archivo estático 'frontend/index.html' se servirá en ''' al
# montar 'StaticFiles' al final de este módulo. Eliminamos la ruta raíz
# explícita para que las peticiones a `/` devuelvan la página del frontend.

@app.get("/characters", response_model=List[Character])
def list_characters():
    """ Lista todos los personajes."""
    return service.list_characters()

@app.get("/characters/{char_id}", response_model=Character)
def get_character(char_id: int):
    """ Obtiene un personaje por su ID."""
    item = service.get_character(char_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")
    return item

@app.post("/characters", response_model=Character, status_code=status.HTTP_201_CREATED)
def create_character(payload: CharacterCreate):
    """ Crea un nuevo personaje."""
    return service.create_character(payload)

@app.put("/characters/{char_id}", response_model=Character)
def update_character(char_id: int, payload: CharacterUpdate):
    """ Actualiza un personaje existente."""
    updated = service.update_character(char_id, payload)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")
    return updated

@app.delete("/characters/{char_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_character(char_id: int):
    """ Elimina un personaje por su ID."""
    ok = service.delete_character(char_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")
    return None

@app.get("/docs/", include_in_schema=False)
def _docs_slash_redirect():
    """Agrego esta función para redirigir `/docs/` a `/docs` y evitar
    problemas con rutas que terminan en `/`.
    """
    return RedirectResponse(url="/docs")

# Monta el frontend estático en la raíz (`/`). El montaje se realiza después
# del registro de rutas para que las rutas de la API (incluyendo `/docs`)
# tengan prioridad.
frontend_dir = BASE_DIR / "frontend"
app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")