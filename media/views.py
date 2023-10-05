from django.http import QueryDict, JsonResponse, HttpResponse
from django.shortcuts import render

from media.services import ImageService
from tickets.services import TicketService


def images_view(request):
    if request.method == "DELETE":
        req_data = QueryDict(request.body)
        ImageService().delete_image(request.user, req_data["id"])
        return JsonResponse({}, status=204)
    elif request.method == "POST":
        ticket_id = request.POST["ticket_id"]
        ImageService().store_images(request.user, ticket_id, request.FILES.getlist("files[]"))
        return JsonResponse({}, status=200)
    return HttpResponse(status=405)
