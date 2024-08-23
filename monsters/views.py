from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Monster
from .serializers.monsters_serializer import MonsterSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def monster_list_create(request):
    if request.method == 'GET':
        monsters = Monster.objects.all()
        serializer = MonsterSerializer(monsters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = MonsterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def monster_detail(request, pk):
    try:
        monster = Monster.objects.get(pk=pk)
    except Monster.DoesNotExist:
        return Response({'error': 'Monster not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MonsterSerializer(monster)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = MonsterSerializer(monster, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = MonsterSerializer(monster, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        monster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

