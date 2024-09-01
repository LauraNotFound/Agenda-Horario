from django.urls import path
from .views import task_list
from .views import TaskListView, TaskCreativeView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('new/', TaskCreativeView.as_view(), name='task_create'),
    path('api/tasks', task_list, name='task_list'),
]