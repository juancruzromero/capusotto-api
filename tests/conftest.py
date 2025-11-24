""" Definición de fixtures para tests con pytest. """

import sys
import pathlib
import json
import pytest
from fastapi.testclient import TestClient

# Asegura que el root del repositorio esté en sys.path para que
# los módulos de nivel superior (p. ej. 'service') puedan
# importarse al ejecutar `pytest` desde la terminal.
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import service
import main

@pytest.fixture
def temp_data(tmp_path):
    """Crea un archivo JSON temporal con datos de prueba y parchea
    el módulo de servicio para usarlo. Esto evita modificar el
    archivo real `data/characters.json` durante las pruebas.
    """
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    data_file = data_dir / "characters.json"

    sample = [
        {
            "id": 1,
            "nombre": "Test Person 1",
            "descripcion": "Desc 1",
            "frase": "Frase 1",
            "video": "https://www.youtube.com/watch?v=abc"
        },
        {
            "id": 2,
            "nombre": "Test Person 2",
            "descripcion": "Desc 2",
            "frase": "Frase 2",
            "video": "https://www.youtube.com/watch?v=def"
        }
    ]

    data_file.write_text(json.dumps(sample, ensure_ascii=False, indent=4), encoding="utf-8")

    # Patch service module to use temporary paths
    service.DATA_DIR = data_dir
    service.DATA_FILE = data_file

    yield data_file

@pytest.fixture
def client(temp_data):
    return TestClient(main.app)
