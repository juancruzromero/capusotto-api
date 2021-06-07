
# DRF 
from rest_framework import serializers

from capuapi.personajes.models import Personaje

class PersonajeSerializer(serializers.Serializer):
    name = serializers.CharField()
    about = serializers.CharField()

class CreatePersonajeSerializer(serializers.Serializer):
    name = serializers.CharField()
    about = serializers.CharField()
    
    def create(self, data):
        """Create personaje."""
        return Personaje.objects.create(**data)