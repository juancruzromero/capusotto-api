"""
Personajes Serializers.

DRF Docs: https://www.django-rest-framework.org/api-guide/serializers/#serializers
"""
# DRF 
from rest_framework import serializers
# Models
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