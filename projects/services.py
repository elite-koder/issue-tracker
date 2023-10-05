from projects.models import Project


class ProjectService:
    def create_new_project(self, owner, title, desc):
        return Project.create_project(owner, title, desc)

    def get_all_projects(self, owner):
        return Project.get_all_projects(owner)
