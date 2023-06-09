from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        related_name="customuser_set",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        related_name="customuser_set",
        related_query_name="customuser",
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
