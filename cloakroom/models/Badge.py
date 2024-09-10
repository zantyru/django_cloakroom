from django.utils.translation import gettext_lazy as _
from django.db import models


class Badge(models.Model):
    """
    Номерок, который отдают посетителям взамен принятой на хранение вещи.
    """

    class State(models.TextChoices):
        UNKNOWN = "U", _("Неопределённое состояние")
        LOST = "L", _("Утерян")
        OCCUPIED = "O", _("У клиента")
        READY = "R", _("Готов к выдаче")

    label = models.CharField(max_length=10, unique=True, blank=False, null=False)
    state = models.CharField(max_length=1, choices=State.choices, default=State.UNKNOWN, blank=False, null=False)
