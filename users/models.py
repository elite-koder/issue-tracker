from django.contrib.auth.models import AbstractUser
from django.db import models

from base_models import BaseModel


# Create your models here.
class User(AbstractUser, BaseModel):
    pass

    @classmethod
    def create_user(cls, username):
        user, created = User.objects.get_or_create(username=username)
        if created:
            from projects.models import Project
            Project.create_default_project(user)
        return user.id, created

    def get_session_auth_hash(self):
        return "qwerty"
