from rest_framework import serializers
from .models import (
    Client,
    Project,
    Task
)    

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name']

# It is used in @apiview        
'''        
class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name']
'''

class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.name", read_only=True)
    class Meta:
        model = Project
        fields = ['name', 'description', 'end_date', 'client', 'client_name']

# It is used in @apiview
'''
class ProjectDetailSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.name", read_only=True)
    class Meta:
        model = Project
        fields = ['name', 'description', 'end_date', 'client', 'client_name']
'''        

class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source="project.name", read_only=True)
    class Meta:
        model = Task
        fields = ["name", "description", "project", "status", "project_name"]

# It is used in @apiview
'''
class TaskDetailSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source="project.name", read_only=True)
    class Meta:
        model = Task
        fields = ["name", "description", "project", "status", "project_name"]        
'''        