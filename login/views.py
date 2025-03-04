from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from user.models import CustomUser
from register.formRegistration import RegistrationForm
from courses.models import Course
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
import uuid
from courses.repositories.course_repository import CourseRepository
from register.formRegistration import CustomAuthenticationForm
# Create your views here.


def user_login(request):
    user_active = None
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            ci_or_email = form.cleaned_data.get('ci_or_email')
            password = form.cleaned_data.get('password')

            # Intentamos autenticar con el modelo predeterminado de User
            user = authenticate(request, username=ci_or_email, password=password)
            
            # Si no se encuentra con el modelo User, intentamos con el modelo CustomUser
            if user is None:
                user = CustomUser.objects.filter(ci=ci_or_email).first()
                if user is None:
                    user = CustomUser.objects.filter(email=ci_or_email).first()

                if user and user.password == password:  # Verifica la contraseña manualmente
                    # Si se encuentra un estudiante, iniciamos sesión de forma manual
                    user = CustomUser

            if user is not None:
                login(request, user)
                
                # Establece user_active a True si el usuario está activo
                request.session['user_id'] = user.ci
                user.is_active = True
                user_active = user.is_active
                
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form, 'user_active': user_active})

def user_logout(request):
    user = request.user  # Obtener el usuario actualmente autenticado
    if user.is_authenticated:
        logout(request) 
    return redirect('home')   