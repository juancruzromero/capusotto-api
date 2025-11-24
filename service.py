""" Módulo de servicio para gestionar personajes
almacenados en un archivo JSON."""

from pathlib import Path
from typing import List, Dict, Optional
import json

from models import CharacterCreate, CharacterUpdate

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "characters.json"

def _read_characters() -> List[Dict]:
    """Lee la lista de personajes desde el archivo JSON."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def _write_characters(chars: List[Dict]):
    """Escribe la lista de personajes en el archivo JSON."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(chars, f, ensure_ascii=False, indent=4)

def list_characters() -> List[Dict]:
    """Lista todos los personajes."""
    return _read_characters()

def get_character(char_id: int) -> Optional[Dict]:
    """Obtiene un personaje por su ID."""
    chars = _read_characters()
    for c in chars:
        if c.get("id") == char_id:
            return c
    return None

def create_character(payload: CharacterCreate) -> Dict:
    """Crea un nuevo personaje."""
    chars = _read_characters()
    next_id = max((c.get("id", 0) for c in chars), default=0) + 1
    new = payload.dict()
    new_obj = {"id": next_id, **new}
    chars.append(new_obj)
    _write_characters(chars)
    return new_obj

def update_character(char_id: int, payload: CharacterUpdate) -> Optional[Dict]:
    """Actualiza un personaje existente."""
    chars = _read_characters()
    for i, c in enumerate(chars):
        if c.get("id") == char_id:
            updated = c.copy()
            for k, v in payload.dict(exclude_unset=True).items():
                updated[k] = v
            chars[i] = updated
            _write_characters(chars)
            return updated
    return None

def delete_character(char_id: int) -> bool:
    """Elimina un personaje por su ID."""
    chars = _read_characters()
    for i, c in enumerate(chars):
        if c.get("id") == char_id:
            chars.pop(i)
            _write_characters(chars)
            return True
    return False