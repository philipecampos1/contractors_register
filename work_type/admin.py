from django.contrib import admin
from . import models


class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(models.WorkType, WorkTypeAdmin)
