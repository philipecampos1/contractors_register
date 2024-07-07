from django.db import models
from staircases.models import Staircase
from django.utils import timezone


class Visitor(models.Model):
    name = models.CharField(max_length=150)
    staircase = models.ForeignKey(Staircase, on_delete=models.PROTECT, related_name='visitor')
    telephone_number = models.CharField(max_length=15, blank=True, null=True)
    arriving_time = models.DateTimeField(default=timezone.now)
    leaving_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-arriving_time']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.leaving_time:
            self.is_active = False
        super().save(*args, **kwargs)
