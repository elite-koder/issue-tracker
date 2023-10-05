from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render

from comments.services import CommentService


@login_required
def comments_view(request):
    if request.method == "POST":
        if request.POST["msg"].strip():
            CommentService().create_comment(request.user, request.POST["ticket_id"], request.POST["msg"].strip())
        return JsonResponse({}, status=200)
    elif request.method == "DELETE":
        req_data = QueryDict(request.body)
        CommentService().delete_comment(request.user, req_data["id"])
        return JsonResponse({}, status=204)
    return HttpResponse(status=405)
