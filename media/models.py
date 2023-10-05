from django.db import models

from base_models import BaseModel
from tickets.models import Ticket
from users.models import User


# Create your models here.
class Image(BaseModel):
    filename = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="ticket_images")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_images")

    @classmethod
    def store_image(cls, owner, ticket_id, image):
        cls.objects.create(owner=owner, filename=image.name, image=image, ticket_id=ticket_id)

    @classmethod
    def delete_image(cls, owner, id):
        cls.objects.filter(owner=owner, id=id).delete()
