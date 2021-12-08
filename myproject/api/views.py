from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import (
    Client,
    Project,
    Task
)    
from .serializers import (
    ClientSerializer, 
    ClientDetailSerializer, 
    ProjectSerializer, 
    ProjectDetailSerializer,
    TaskSerializer,
    TaskDetailSerializer
)

@api_view(['GET', 'POST'])
def clients_view(request):

    if request.method == 'GET':
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = serializer.save()   
            return Response(ClientSerializer(client, many=True).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
 
@api_view(['GET', 'PATCH', 'DELETE'])
def client_detail_view(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'GET':
        serializer = ClientDetailSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = ClientDetailSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            client = serializer.save()
            return Response(ClientDetailSerializer(client).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response("Client Deleted", status=status.HTTP_204_NO_CONTENT)    

@api_view(['GET', 'POST'])
def projects_view(request):

    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def project_detail_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'GET':
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = ProjectDetailSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            project = serializer.save()
            return Response(ProjectDetailSerializer(project).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response("Project Deleted", status=status.HTTP_204_NO_CONTENT)            

@api_view(['GET', 'POST'])
def task_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'GET':
        tasks = Task.objects.filter(project=project_id)
        serializer  = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

@api_view(['GET', 'PATCH', 'DELETE'])
def task_detail_view(request, project_id, task_id):
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'GET':
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = TaskDetailSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            task = serializer.save()
            return Response(TaskDetailSerializer(task).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response("Task Deleted", status=status.HTTP_204_NO_CONTENT)            
