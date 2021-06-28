""" Personajes views. """
# DRF
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# DRF - Permissions
from rest_framework.permissions import IsAuthenticated
# Models
from capuapi.personajes.models import Personaje
# Serializers
from capuapi.personajes.serializers import (PersonajeSerializer,
                                            CreatePersonajeSerializer)

@api_view(['GET'])
def list_personajes(request):
    """Listar personajes

    Args:
        request (request): Request que ingresa de algún cliente.

    Returns:
        dict: Lista de personajes.
    """
    personajes = Personaje.objects.all()
    serializer = PersonajeSerializer(personajes, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def personaje_detail_view(request, pk=None):
    """Detalle por personaje.

    Args:
        request (request): Request que ingresa de algún cliente.
        pk ([type], optional): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    if request.method == 'GET':
        print(f"Mostrar personaje:{pk}")
        personaje = Personaje.objects.filter(id=pk).first()
        personaje_serializer = PersonajeSerializer(personaje)
        return Response(personaje_serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_personaje(request):
    """Crear personaje.

    Args:
        request (request): Request que ingresa de algún cliente.

    Returns:
        dict: Personaje creado.
    """
    serializer = CreatePersonajeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    personaje = serializer.save()
    return Response(PersonajeSerializer(personaje).data)

@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def modify_personaje(request, pk=None):
    """Modificar o eliminar personaje.

    Args:
        request (request): Request que ingresa de algún cliente.
        pk (str, optional): Indica el id a modificar o
        borrar. Defaults to None.

    Returns:
        str: Respuesta de la acción.
    """
    if request.method == 'PUT':
        # Aún no es necesario.
        # TODO: Seguir viendo https://www.youtube.com/watch?v=rOoRSQeU2ds&list=PLMbRqrU_kvbRI4PgSzgbh8XPEwC1RNj8F&index=7
        pass
    elif request.method == 'DELETE':
        personaje = Personaje.objects.filter(id=pk).first()
        personaje.delete()
        return Response('Eliminado')