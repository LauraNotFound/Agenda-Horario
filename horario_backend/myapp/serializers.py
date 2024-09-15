from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' # Aquí tuve un error que me tomó encontrar toda una mañana, había escrito field en lugar de fiels que refiere a todas los campos a llamar, en este caso llamo a actividad, dia, hora, color