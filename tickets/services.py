from tickets.models import Ticket, TicketStatus, TicketPriority
from tickets.utils import get_unique_filename


class TicketService:
    def get_all_tickets(self, owner, project_id, status, priority):
        return Ticket.get_all_tickets(owner, project_id, status, priority)

    def create_new_ticket(self, owner, title, desc, project_id, images):
        for image in images:
            image.name = get_unique_filename(image.name)
        Ticket.create_new_ticket(owner, title, desc, project_id, images)

    def update_ticket(self, owner, id, data):
        Ticket.update_ticket(owner, id, data)

    def get_ticket_statutes(self):
        return [_.value for _ in TicketStatus]

    def get_ticket_priorities(self):
        return [_.value for _ in TicketPriority]

    def get_ticket_details(self, owner, id):
        return Ticket.get_details(owner, id)

    def delete_ticket(self, owner, id):
        Ticket.delete_ticket(owner, id)
