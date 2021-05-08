from capuapi.utils.models import CapuAPIModel

class Personaje(CapuAPIModel):
    """ TODO: Documentar...
    """
    name = models.CharField('nombre', max_length=140)

    def __str__(self):
        """Return circle name."""
        return self.name

    class Meta(CapuAPIModel.Meta):
        pass