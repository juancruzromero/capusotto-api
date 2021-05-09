
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from capuapi.personajes.models import Personaje

# Serializares
from capuapi.personajes.serializers import PersonajeSerializer

@api_view(['GET'])
def list_personajes(request):
    """Listar Personajes.
    """
    personajes = Personaje.objects.filter()
    serializer = PersonajeSerializer(personajes, many=True)

    return Response(serializer)