""" Pruebas para la API de personajes. """

def test_list_characters(client):
    """ Prueba la obtención de la lista de personajes. """
    r = client.get("/characters")
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, list)
    assert len(body) == 2

def test_get_character_found(client):
    """ Prueba la obtención de un personaje existente. """
    r = client.get("/characters/1")
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert body["nombre"] == "Test Person 1"

def test_get_character_not_found(client):
    """ Prueba la obtención de un personaje inexistente. """
    r = client.get("/characters/999")
    assert r.status_code == 404

def test_create_character(client):
    # TODO: Implementar cuando tengamos la base de datos.
    pass

def test_update_character(client):
    """ Prueba la actualización de un personaje existente. """
    payload = {"frase": "Updated phrase"}
    r = client.put("/characters/1", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["frase"] == "Updated phrase"

def test_delete_character(client):
    """ Prueba la eliminación de un personaje existente. """
    r = client.delete("/characters/2")
    assert r.status_code == 204

    r2 = client.get("/characters/2")
    assert r2.status_code == 404