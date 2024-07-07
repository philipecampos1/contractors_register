from django.contrib import admin
from . import models


class ContractorAdmin(admin.ModelAdmin):
    list_display = ['work_code', 'company', 'is_active',]
    search_fields = ['work_code', 'company__name',]


admin.site.register(models.Contractor, ContractorAdmin)
