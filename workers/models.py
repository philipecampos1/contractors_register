from django.db import models
from staircases.models import Staircase


class Worker(models.Model):
    name = models.CharField(max_length=200)
    telephone_number = models.CharField(max_length=15, null=True, blank=True)
    staircase = models.ForeignKey(Staircase, on_delete=models.PROTECT, related_name='worker')
    email = models.EmailField(null=True, blank=True, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
