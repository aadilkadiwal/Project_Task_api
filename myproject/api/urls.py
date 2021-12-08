from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.clients_view, name='clients_view'),
    path('clients/<int:client_id>/', views.client_detail_view, name='client_detail_view'),
    path('projects/', views.projects_view, name='projects_view'),
    path('projects/<int:project_id>/', views.project_detail_view, name='project_detail_view'),
    path('projects/<int:project_id>/tasks/', views.task_view, name='task_view'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail_view, name='task_detail_view'),
]