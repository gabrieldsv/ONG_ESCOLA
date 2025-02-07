from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('coordenador', 'Coordenador'),
        ('professor', 'Professor'),
        ('assistente_social', 'Assistente Social'),
        ('profissional_saude', 'Profissional de Saúde'),
    )
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.username