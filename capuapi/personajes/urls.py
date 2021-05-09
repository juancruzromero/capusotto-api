"""URLs de personajes"""

# Django
from django.urls import path

# Views
from capuapi.personajes.views import list_personajes

urlpatterns = [
    path('personajes/', list_personajes),
]