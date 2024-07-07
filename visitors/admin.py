from django.contrib import admin
from . import models


class VisitorAdmin(admin.ModelAdmin):
    list_display = ['name', 'staircase', 'is_active']
    search_fields = ['name', 'staircase__name']


admin.site.register(models.Visitor, VisitorAdmin)
