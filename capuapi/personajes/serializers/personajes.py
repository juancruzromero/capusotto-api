
# DRF 
from rest_framework import serializers

from capuapi.personajes.models import Personaje

class PersonajeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    about = serializers.CharField()
    video_url = serializers.CharField()

class CreatePersonajeSerializer(serializers.Serializer):
    name = serializers.CharField()
    about = serializers.CharField()
    video_url = serializers.CharField()

    def create(self, data):
        """Create personaje."""
        return Personaje.objects.create(**data)