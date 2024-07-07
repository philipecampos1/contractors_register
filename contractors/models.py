from django.db import models
from dirtyfields import DirtyFieldsMixin
from work_type.models import WorkType
from staircases.models import Staircase
from workers.models import Worker
from company.models import Company
from django.utils import timezone


class Contractor(DirtyFieldsMixin, models.Model):
    work_type = models.ForeignKey(WorkType, on_delete=models.PROTECT, related_name='contractor')
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='contractor')
    work_code = models.CharField(max_length=10)
    work_reason = models.CharField(max_length=500)
    responsible_worker = models.ForeignKey(Worker, on_delete=models.PROTECT, related_name='contractor')
    contractor_name = models.CharField(max_length=200, blank=True, null=True)
    contractor_number = models.CharField(max_length=15, blank=True, null=True)
    expected_arriving_time = models.DateTimeField(default=timezone.now)
    arriving_time = models.DateTimeField(blank=True, null=True)
    leaving_time = models.DateTimeField(blank=True, null=True)
    staircase = models.ForeignKey(Staircase, on_delete=models.PROTECT, related_name='contractor')
    location = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    in_the_building = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.work_reason
