from api import viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('clients', viewsets.ClientViewSet, basename='clients')
router.register('projects', viewsets.ProjectViewSet, basename='projects')
router.register('tasks', viewsets.TaskViewSet, basename='tasks')