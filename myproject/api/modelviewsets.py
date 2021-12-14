from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from  .serializers import (
    ClientSerializer,
    ProjectSerializer,
    TaskSerializer
)
from .models import (
    Client,
    Project,
    Task
)
from .paginations import (
    MyCursorPagination,
    MyLimitOffsetPagination,
    MyPageNumberPagination
)    

class ClientModelViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = MyLimitOffsetPagination

    # To override create function for posting multiple client json input
    def create(self, request):

        # To check input (POST) is in list form or dict form
        if isinstance(request.data, list):
            serializer = ClientSerializer(data=request.data, many=True)
        else:
            serializer = ClientSerializer(data=request.data) 
        # To check the data is valid or not    
        if serializer.is_valid():
            # To save validated data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is not valid then Response will be an error page    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # To get only those client whose id is less then 11
    def get_queryset(self):
        return Client.objects.filter(pk__lt=11) 

class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = MyPageNumberPagination

    # To override create function for posting multiple project json input
    def create(self, request):

        # To check input (POST) is in list form or dict form
        if isinstance(request.data, list):
            serializer = ProjectSerializer(data=request.data, many=True)
        else:
            serializer = ProjectSerializer(data=request.data) 
        # To check the data is valid or not    
        if serializer.is_valid():
            # To save validated data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is not valid then Response will be an error page    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # This function is use for nested pk value
    @action(detail=True, methods=["GET"])
    def tasks(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        tasks = Task.objects.filter(project=project)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # To get only those project whose id is 9,11,12,13,14,15
    def get_queryset(self):
        return Project.objects.filter(pk__in=[9,11,12,13,14,15])

class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer
    pagination_class = MyCursorPagination       

    # To override create function for posting multiple task json input
    def create(self, request):

        # To check input (POST) is in list form or dict form
        if isinstance(request.data, list):
            serializer = TaskSerializer(data=request.data, many=True)
        else:
            serializer = TaskSerializer(data=request.data) 
        # To check the data is valid or not    
        if serializer.is_valid():
            # To save validated data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is not valid then Response will be an error page    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # To get all of those task whose id is greater than 0
    def get_queryset(self):
        return Task.objects.filter(pk__gt=0)    
