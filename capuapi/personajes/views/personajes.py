
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from capuapi.personajes.models import Personaje

# Serializares
from capuapi.personajes.serializers import PersonajeSerializer, CreatePersonajeSerializer

@api_view(['GET'])
def list_personajes(request):
    """Listar Personajes.
    """
    personajes = Personaje.objects.all()
    serializer = PersonajeSerializer(personajes, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def create_personaje(request):
    """Crear personaje."""
    serializer = CreatePersonajeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    personaje = serializer.save()
    return Response(PersonajeSerializer(personaje).data)