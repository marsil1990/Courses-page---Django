from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password

class UserFactory:
    @staticmethod
    def create_user(ci,password, first_name, last_name, email, description = None, active=True, isStaff=False, role=None) :
        """
        Factory Method para crear instancias del modelo CutomUser con reglas de negocio específicas.
        """
        if description is None:
            description = f"{first_name} is a {role}."
        # Validación de dificultad
        if role == 'Teacher':
            user = CustomUser.objects.create(ci=ci, password=make_password(password), first_name=first_name, last_name = last_name, email =email, description=description, role=role)
        else:
           user = CustomUser.objects.create(ci=ci, password=make_password(password), first_name=first_name, last_name = last_name, email =email, description=description, role=role)
            
    
        return user
    