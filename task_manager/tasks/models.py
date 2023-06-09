from django.db import models
from django.urls import reverse
from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from task_manager.users.models import CustomUser
from django.utils.translation import gettext_lazy as _


class Tasks(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Name"),
    )
    description = models.TextField(verbose_name=_("Description"))
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True)
    status = models.ForeignKey(
        Statuses,
        on_delete=models.PROTECT,
        verbose_name=_("Status"),
    )
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        null=True,
        related_name="executor",
        verbose_name=_("Executor"),
    )
    labels = models.ManyToManyField(
        Labels, through="LabelForTask", verbose_name=_("Labels"), blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("tasks")


class LabelForTask(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    labels = models.ForeignKey(Labels, on_delete=models.PROTECT)
