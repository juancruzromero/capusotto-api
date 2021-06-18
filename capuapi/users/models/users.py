"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from capuapi.utils.models import CapuAPIModel

class User(CapuAPIModel, AbstractUser):
    """
    Personalizo la autenticación heredando el model 'User' que ofrece Django.
    Doc: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con ese e-mail.'
        }
    )

    # Valido número.
    # Doc de Validators: https://docs.djangoproject.com/en/3.2/ref/validators/
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='El teléfono debe tener este formato: +999999999. No más de 15 caracteres.'
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#django.contrib.auth.models.CustomUser.USERNAME_FIELD
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Se pasa a True cuando se valida el usuario con mail.'
    )

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username