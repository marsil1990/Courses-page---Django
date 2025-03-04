# VIEWS
from paypal.standard.forms import PayPalPaymentsForm
@login_required(login_url='/login/')
def register_course(request, nameCourse):
    if RegisterCourse.objects.filter(CustomUser = request.user, course = nameCourse):
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
    RegisterCourse.objects.create(course = course, CustomUser=user)
    return render(request, 'paymentSuccessful.html', {"product":nameCourse})


#URLS
urlpatterns = [
    path('register/', views.register, name='register' ),
    path('register_course/<str:nameCourse>/', views.register_course, name='register_course'),
    path('paymentFailed/<str:nameCourse>/', views.paymentFailed, name='paymentFailed'),
    path('paymentSuccessful/<str:nameCourse>/', views.paymentSuccessfull, name='paymentSuccessful'),
    
]

#APPS
INSTALLED_APPS = [
    'paypal.standard.ipn',
    'polymorphic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'lessons.apps.LessonsConfig',
    'exercises.apps.ExercisesConfig', 
    'user',
    'register',
    'login',
    'courses',
]

#SETTING
PAYPAL_RECEIVER_EMAIL = config('PAYPAL_RECEIVER_EMAIL')
PAYPAL_TEST = config('PAYPAL_TEST', cast=bool)
PAYPAL_BUY_BUTTON_IMAGE = config('PAYPAL_BUY_BUTTON_IMAGE')
#PAYPAL_RECEIVER_EMAIL='sb-43bqq715379907@business.example.com'
#PAYPAL_TEST = True

#PAYPAL_BUY_BUTTON_IMAGE= "https://www.paypal.com/en_US/i/btn/btn_paynowCC_LG.gif"
#PAYPAL_BUY_BUTTON_IMAGE'https://res.cloudinary.com/the-proton-guy/image/upload/v1685882223/paypal-PhotoRoom_v9pay7.png'