from django.contrib.auth.models import AbstractUser, Group
from django.db import models
import uuid


class CustomUser(AbstractUser):
    pass


class Invitation(models.Model):
    email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True, blank=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.email
