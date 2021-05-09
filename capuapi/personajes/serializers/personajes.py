
# DRF 
from rest_framework import serializers

from capuapi.personajes.models import Personaje

class PersonajeSerializer(serializers.Serializer):
    name = serializers.CharField()
    about = serializers.CharField()