""" Django model utility for don't repeat code """

from django.db import models

class CapuAPIModel(models.Model):
    """
    Fields de Django: https://docs.djangoproject.com/en/3.2/ref/forms/fields/
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Fecha de creación.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Fecha de última modificación.'
    )

    class Meta:
        """Opciones para Metadata.
        """
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']    