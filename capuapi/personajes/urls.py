"""URLs de personajes"""

# Django
from django.urls import path

# Views
from capuapi.personajes.views import list_personajes, create_personaje

urlpatterns = [
    path('personajes/', list_personajes),
    path('personajes/create/', create_personaje)
]