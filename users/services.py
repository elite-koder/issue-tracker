from users.models import User


class UserService:
    def create_user(self, username):
        return User.create_user(username)
