from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомизированная модель пользователя."""
    auth_token = models.CharField(max_length=256, unique=True, verbose_name='Токен авторизации')
    data = models.JSONField(null=True, verbose_name='Данные ИМТ')
