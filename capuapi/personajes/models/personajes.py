# Django
from django.db import models

# Utilities
from capuapi.utils.models import CapuAPIModel

class Personaje(CapuAPIModel):
    """ TODO: Documentar...
    """
    name = models.CharField('nombre', max_length=140)
    about = models.CharField('descripcion personaje', max_length=255)

    def __str__(self):
        """Return circle name."""
        return self.name

    class Meta(CapuAPIModel.Meta):
        pass