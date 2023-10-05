from django.db import models, IntegrityError

from base_models import BaseModel
from projects.errors import DuplicateProjectError
from users.models import User


class Project(BaseModel):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

    class Meta:
        unique_together = ['owner', 'title']

    @classmethod
    def create_project(cls, owner, title, desc):
        try:
            return Project.objects.create(owner=owner, title=title, desc=desc).id
        except IntegrityError:
            raise DuplicateProjectError

    @classmethod
    def get_all_projects(cls, owner):
        return Project.objects.filter(owner=owner).values("id", "title", "desc", "created_at")

    @classmethod
    def create_default_project(cls, owner):
        Project.objects.create(owner=owner, title="Project0", desc="Default Project can't delete it.")


# class ProjectContributorMapping(BaseModel):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributors')
#     contributor = models.ManyToManyField(User)
