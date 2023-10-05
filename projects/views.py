from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from projects.errors import DuplicateProjectError
from projects.services import ProjectService


def projects_view(request):
    if request.method == "GET":
        return JsonResponse({"projects": ProjectService().get_all_projects(request.user)})
    elif request.method == 'POST':
        project_id = ""
        try:
            if request.POST['title'].strip():
                project_id = ProjectService().create_new_project(request.user, request.POST['title'].strip(), request.POST['desc'].strip())
            error = False
            msg = "Hurrah!!! Create new project successfully"
        except DuplicateProjectError:
            error = True
            msg = "Hiss!!! Duplicate project found."
        return JsonResponse({"error": error, "msg": msg, "id": project_id}, status=400 * error + 200 * (not error))
    return HttpResponse(content="Method Not Allowed", status=405)
