from django.contrib import admin
from .models import Task
# Register your models here. Registra tus modelos aquí

class TaskAdmin(admin.ModelAdmin):
    list_display = ('actividad', 'dia', 'hora', 'color')
    search_fields = ('actividad',)

admin.site.register(Task, TaskAdmin)
