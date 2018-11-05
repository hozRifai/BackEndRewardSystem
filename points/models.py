from django.db import models
from django.conf import settings

# Create your models here.
from django.core.validators import (
    RegexValidator,
    MinValueValidator,
    MaxValueValidator
    )

User = settings.AUTH_USER_MODEL


class Points(models.Model):
    accountNumber = models.ForeignKey(User, to_field="account_no", on_delete=models.CASCADE)
    username = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE, related_name="usernames")
    amount = models.PositiveIntegerField(
        validators=[
            MinValueValidator(00000000),
            MaxValueValidator(99999999)
            ]
    )

    def __str__(self):
        return str(self.accountNumber)