# Django
from django.db import models
# Utilities
from capuapi.utils.models import CapuAPIModel

class Personaje(CapuAPIModel):
    """Personaje Model. Indico la composición del modelo
    de personajes.

    Args:
        CapuAPIModel (obj): Herencia de datos básicos para
        completar el model.

    Returns:
        str: Retorna el nombre.
    """
    name = models.CharField('nombre', max_length=140)
    about = models.CharField('acerca del personaje', max_length=255)
    video_url = models.CharField('video de presentación', max_length=255)

    def __str__(self):
        """Return circle name."""
        return self.name

    class Meta(CapuAPIModel.Meta):
        pass