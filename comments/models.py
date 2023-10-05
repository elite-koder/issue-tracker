from django.db import models

from base_models import BaseModel
from tickets.models import Ticket
from users.models import User


class Comment(BaseModel):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="ticket_comments")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    msg = models.CharField(max_length=300)

    @classmethod
    def add_comment(cls, owner, ticket_id, msg):
        Comment.objects.create(owner=owner, ticket_id=ticket_id, msg=msg)

    @classmethod
    def delete_comment(cls, owner, id):
        Comment.objects.filter(owner=owner, id=id).delete()

    @classmethod
    def get_comments(cls, ticket_id):
        return Comment.objects.filter(ticket_id=ticket_id).order_by("-id").values("id", "msg", "owner", "created_at")
