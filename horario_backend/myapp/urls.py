from django.urls import path
from .views import task_list, TaskListView, TaskCreativeView, api_root
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('new/', TaskCreativeView.as_view(), name='task_create'),
    path('api/', api_root,  name='api_root'),
    path('api/tasks/', task_list, name='task_list_api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)