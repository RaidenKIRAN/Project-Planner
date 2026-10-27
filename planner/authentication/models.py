from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoices(models.TextChoices):

    DEVELOPER = "Developer","Developer"
    ADMIN = "Admin","Admin",
    PROJECT_COORDINATOR = 'Project Coordinator','Project Coordinator'

class Profile(AbstractUser):

    role = models.CharField(max_length=20, choices=RoleChoices.choices)

    def __str__(self):

        return self.username

    class Meta:

        verbose_name_plural = "categories"