from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from .models import (
    Client,
    Project,
    Task
)    
from .serializers import (
    ClientSerializer,
    ProjectSerializer,
    TaskSerializer
)

class ClientViewSet(viewsets.ViewSet):

    def list(self, request):

        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        client = get_object_or_404(Client, pk=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def create(self, request):

        if isinstance(request.data, list):
            serializer = ClientSerializer(data=request.data, many=True)
        else:
            serializer = ClientSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):

        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):

        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                               
    
    def destroy(self, request, pk):

        client = Client.objects.get(pk=pk)
        client.delete()
        return Response("Client Deleted", status=status.HTTP_204_NO_CONTENT)

class ProjectViewSet(viewsets.ViewSet):

    def list(self, request):

        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def create(self, request):

        if isinstance(request.data, list):
            serializer = ProjectSerializer(data=request.data, many=True)
        else:
            serializer = ProjectSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):

        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):

        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                               
    
    def destroy(self, request, pk):

        project = Project.objects.get(pk=pk)
        project.delete()
        return Response("Project Deleted", status=status.HTTP_204_NO_CONTENT)   

    @action(detail=True, methods=["GET"])
    def tasks(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        tasks = Task.objects.filter(project=project)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)       
    
class TaskViewSet(viewsets.ViewSet):

    def list(self, request):

        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        task= get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def create(self, request):

        if isinstance(request.data, list):
            serializer = TaskSerializer(data=request.data, many=True)
        else:
            serializer = TaskSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):

        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):

        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                               
    
    def destroy(self, request, pk):

        task = Task.objects.get(pk=pk)
        task.delete()
        return Response("Task Deleted", status=status.HTTP_204_NO_CONTENT)
