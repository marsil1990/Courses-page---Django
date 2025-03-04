from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class CustomUserAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            CustomUser = User.objects.get(Q(email=username) | Q(ci=username)) 
        except User.DoesNotExist:
            return None

        if CustomUser.check_password(password):
            return CustomUser
        else:
            return None