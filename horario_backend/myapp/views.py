from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

#Agregado para API
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Task
#Agregado para API
from .serializers import TaskSerializer

from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskCreativeView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

#Agregado para API
@api_view(['GET', 'POST'])

def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)