from django.contrib import admin
from . import models
# Register your models here.


class StaircaseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(models.Staircase, StaircaseAdmin)
