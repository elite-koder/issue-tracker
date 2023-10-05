from media.models import Image
from tickets.utils import get_unique_filename


class ImageService:
    def delete_image(self, owner, id):
        Image.delete_image(owner, id)

    def store_images(self, owner, ticket_id, images):
        for image in images:
            image.name = get_unique_filename(image.name)
            Image.store_image(owner, ticket_id, image)
