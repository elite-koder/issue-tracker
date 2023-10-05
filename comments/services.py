from comments.models import Comment


class CommentService:
    def create_comment(self, owner, ticket_id, msg):
        Comment.add_comment(owner, ticket_id, msg)

    def delete_comment(self, owner, id):
        Comment.delete_comment(owner, id)

    def get_comments(self, ticket_id):
        return Comment.get_comments(ticket_id)
