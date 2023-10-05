from django.db import models, transaction
from django.db.models import F

from base_models import BaseModel
from projects.models import Project
from users.models import User


class TicketStatus(models.TextChoices):
    OPEN = 'OPEN'
    WIP = 'WIP'
    CLOSED = 'CLOSED'


class TicketPriority(models.TextChoices):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'


class TicketType(models.TextChoices):
    BUG = 'BUG'
    FEATURE_REQUEST = 'FEATURE_REQUEST'


class Ticket(BaseModel):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_tickets")
    status = models.CharField(choices=TicketStatus.choices, max_length=50)
    priority = models.CharField(choices=TicketPriority.choices, max_length=20)
    ticket_type = models.CharField(choices=TicketType.choices, max_length=50, null=True)
    assignee = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="assigned_tickets")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tickets")

    @classmethod
    def get_all_tickets(cls, owner, project_id, status, priority):
        tickets = Ticket.objects.filter(owner=owner)
        if project_id:
            tickets = tickets.filter(project_id=project_id)
        if status:
            tickets = tickets.filter(status=status)
        if priority:
            tickets = tickets.filter(priority=priority)
        tickets.order_by("created_at")
        return tickets.values("id", "title", "desc", "status", "priority", "ticket_type", "assignee", "project_id", project_title=F("project__title"))

    @classmethod
    def create_new_ticket(cls, owner, title, desc, project_id, images):
        from media.models import Image
        with transaction.atomic():
            ticket = Ticket.objects.create(owner=owner, title=title, desc=desc, priority=TicketPriority.LOW, status=TicketStatus.OPEN, project_id=project_id)
            for image in images:
                Image.store_image(owner, ticket.id, image)
    @classmethod
    def update_ticket(cls, owner, id, data):
        Ticket.objects.filter(owner=owner, id=id).update(**data)

    @classmethod
    def get_details(cls, owner, id):
        from media.models import Image
        ticket = Ticket.objects.filter(owner=owner, id=id).values("id", "title", "desc", "status", "priority", "ticket_type", "assignee", "project_id").first()
        ticket["images"] = Image.objects.filter(ticket_id=id)
        return ticket

    @classmethod
    def delete_ticket(cls, owner, id):
        Ticket.objects.filter(owner=owner, id=id).delete()
