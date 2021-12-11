from api import modelviewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('clients', modelviewsets.ClientModelViewSet, basename='clients')
router.register('projects', modelviewsets.ProjectModelViewSet, basename='projects')
router.register('tasks', modelviewsets.TaskModelViewSet, basename='tasks')