from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class CustomStudentAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            student = User.objects.get(Q(email=username) | Q(ci=username)) 
        except User.DoesNotExist:
            return None

        if student.check_password(password):
            return student
        else:
            return None