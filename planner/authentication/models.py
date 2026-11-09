from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoices(models.TextChoices):

    DEVELOPER = "Developer","Developer"
    ADMIN = "Admin","Admin",
    PROJECT_COORDINATOR = 'Project Coordinator','Project Coordinator'


class TechChoices(models.TextChoices):

    FRONTEND = 'frontend developer','frontend developer'
    BACKEND = 'backend developer','backend developer'
    FULLSTACK = 'fullstack developer','fullstack developer'
    UIUX = 'UI/UX Designer','UI?UX Designer'
    TESTER = 'tester','tester'



class Profile(AbstractUser):

    role = models.CharField(max_length=20, choices=RoleChoices.choices)

    tech = models.CharField(max_length=20, choices=TechChoices.choices,null=True,blank=True)

    def __str__(self):

        return f'{self.username}-{self.role}-{self.tech}'

    class Meta:

        verbose_name_plural = "Profiles"