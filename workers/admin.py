from django.contrib import admin
from . import models


class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'staircase', 'telephone_number']
    search_fields = ['name']


admin.site.register(models.Worker, WorkerAdmin)
