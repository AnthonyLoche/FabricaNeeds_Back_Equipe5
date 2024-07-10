from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Usuario(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(_("e-mail address"), unique=True)
    passage_id = models.CharField(max_length=255, unique=True)
    picture = models.URLField(blank=True, null=True)
    github_id = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]
