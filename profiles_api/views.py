from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets


class HelloApiView(APIView):
    '''Test APIView'''
    # теперь появиться форма для отправки POST-запроса
    serializer_class = serializers.HelloSerializer
# something with HTTP

    def get(self, request, format=None):
        '''Return a list of APIView'''
        an_apiview = [
            'Uses HTTP method as  funcs (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control logic',
            'Is mapped manually yo URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        '''Create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # получаем проверенный атрибут name из класса
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''Handle updating and object'''
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        '''Handle a partial update of an object'''
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        '''Delete an object'''
        return Response({'method':'DELETE'})

                            # Base Django-class that provides
class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''
    # теперь появиться форма
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''Return a hello messsage'''
        a_viewset = [
            'Uses actions...',
            'Automatically maps to URLs',
            'Provides more funcs'
        ]

        return Response({'message': 'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        '''Create a new hello message'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        '''Handle getting an object by its ID'''
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':'PACTH'})

    def destroy(self, request, pk=None):
        return Response({'http_method':'DELETE'})
