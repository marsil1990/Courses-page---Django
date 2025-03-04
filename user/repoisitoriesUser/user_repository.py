from user.models import CustomUser


class UserRepository:
    @staticmethod
    def getUser(email, role):
        user = CustomUser.objects.get(email = email, role = role)
        return user