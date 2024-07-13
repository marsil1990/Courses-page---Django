from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .formRegistration import RegistrationForm
from .models import Student, Register
from core.models import Course
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
import uuid

def register(request):
    user_active= False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            ci = form.cleaned_data['ci']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            Student.objects.create(ci=ci, password=make_password(password), first_name=first_name, last_name = last_name, email =email, description=description)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form, "user_active":user_active})



from .formRegistration import CustomAuthenticationForm
def user_login(request):
    user_active = False  # Inicializa user_active a False por defecto
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            ci_or_email = form.cleaned_data.get('ci_or_email')
            password = form.cleaned_data.get('password')
            
            # Autentica al usuario
            user = authenticate(request, username=ci_or_email, password=password)
            
            if user is not None:
                # Inicia sesión manualmente
                login(request, user)
                
                # Establece user_active a True si el usuario está activo
                request.session['user_id'] = user.ci
                user.set_is_active(True)
                user_active = Student.get_is_active(user.ci)
               
                
                # Redirige al usuario a la página de inicio
                return redirect('home')  
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form, 'user_active': user_active})


@login_required(login_url='/login/')
def profile(request):
    user = request.user
    student = Student.objects.get(email = user)
    student_ci = student.ci
    student_first_name = student.first_name
    student_last_name = student.last_name
    student_email = student.email
    courses_progress = Course.courses_progress(student=student)
    
    return render(request, 'profile.html', {
        "ci":student_ci,
        "first_name":student_first_name,
        "last_name":student_last_name,
        "email":student_email,
        "courses_progress":courses_progress
    }
)


@login_required(login_url='/login/')
def register_course(request, nameCourse):
    if Register.objects.filter(student = request.user, course = nameCourse):
        return HttpResponse("Already registered for this course.")
    else: 
        host = request.get_host()
        paypal_checkout ={
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': 1,
            'item_name':nameCourse,
            'invoice':uuid.uuid4(),
            'currency_code':'USD',
            'notify_url':f"http://{host}{reverse('paypal-ipn')}",
            'return_url':f"http://{host}{reverse('paymentSuccessful',kwargs={'nameCourse':nameCourse})}",
            'cancel_url':f"http://{host}{reverse('paymentFailed',kwargs={'nameCourse':nameCourse})}",
        }
        paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request, 'register_course.html', {"paypal":paypal_payment})

def paymentFailed(request, nameCourse):
    return render(request, 'paymentFailed.html', {"product":nameCourse})

def paymentSuccessfull(request, nameCourse):
    user =  request.user
    course = Course.objects.get(name = nameCourse)
    Register.objects.create(course = course, student=user)
    return render(request, 'paymentSuccessful.html', {"product":nameCourse})



def user_logout(request):
    #ci= request.session['user_id']
    #Student.set_is_active(ci, False)
    #logout(request)
    user = request.user  # Obtener el usuario actualmente autenticado
    if user.is_authenticated:
        user.set_is_active(False) # Desactivar al usuario
        logout(request) 
    
    return redirect('home')    


