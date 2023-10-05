from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render, redirect

from comments.services import CommentService
from projects.services import ProjectService
from tickets.services import TicketService


@login_required
def tickets_view(request):
    if request.method == 'GET':
        project_id = request.GET.get('project_id')
        ticket_status = request.GET.get("status", "").strip()
        ticket_priority = request.GET.get('priority', '').strip()
        if project_id and project_id.isnumeric():
            project_id = int(project_id)
        else:
            project_id = None
        tickets = TicketService().get_all_tickets(request.user, project_id, ticket_status, ticket_priority)
        projects = ProjectService().get_all_projects(request.user)
        context = {
            "projects": projects,
            "tickets": tickets,
            "statuses": TicketService().get_ticket_statutes(),
            "priorities": TicketService().get_ticket_priorities(),
            "selected_project_id": project_id,
            "selected_status": request.GET.get('status'),
            "selected_priority": request.GET.get('priority'),
        }
        return render(request, "issue_tracker.html", context)
    elif request.method == 'POST':
        resp_data = {"project_id": request.POST['project_id']}
        try:
            if request.POST["title"].strip() and request.POST['project_id']:
                TicketService().create_new_ticket(request.user, request.POST["title"].strip(), request.POST["desc"].strip(), request.POST['project_id'], request.FILES.getlist("files[]"))
            resp_data["error"] = False
            resp_data["msg"] = "Hurrah!!! Created Issue Successfully"
        except Exception as e:
            print(e)
            resp_data["error"] = True
            resp_data["msg"] = "Hiss!!! Please try again after sometime"
        print(resp_data)
        return JsonResponse(resp_data, status=200)
    elif request.method == "PATCH":
        data = {}
        try:
            print(request.FILES)
            # req_data = QueryDict(request.body)
            # keys = ["title", "desc", "status", "priority", "project_id"]
            # data = {key: req_data[key] for key in keys if key in req_data}
            # TicketService().update_ticket(request.user, req_data["id"], data)
            data['error'] = False
            data["msg"] = "Hurrah!!! Updated Successfully"
        except Exception as e:
            print(e)
            data['error'] = True
            data["msg"] = "Hiss!!! Error Occurred. Try again later"
        return JsonResponse(data, status=400*data['error'] + 200*(not data['error']))
    elif request.method == "DELETE":
        data = {}
        try:
            req_data = QueryDict(request.body)
            TicketService().delete_ticket(request.user, req_data["id"])
            data['error'] = False
            data["msg"] = "Hurrah!!! Updated Successfully"
        except Exception as e:
            data['error'] = True
            data["msg"] = "Hiss!!! Error Occurred. Try again later"
        return JsonResponse(data, status=400*data['error'] + 204*(not data['error']))
    return HttpResponse("Method not allowed", status=405)


@login_required
def ticket_edit_view(request, ticket_id):
    if request.method == "GET":
        context = {
            "projects": ProjectService().get_all_projects(request.user),
            "statuses": TicketService().get_ticket_statutes(),
            "priorities": TicketService().get_ticket_priorities(),
            "comments": CommentService().get_comments(ticket_id),
            "ticket": TicketService().get_ticket_details(request.user, ticket_id),
        }
        return render(request, 'edit_issue_modal_body.html', context)
    return HttpResponse(status=405)


@login_required
def redirect_to_home(request):
    if request.method == "GET":
        return redirect("/tickets")
    return HttpResponse(status=405)
