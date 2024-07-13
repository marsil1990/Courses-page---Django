from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register' ),
    path('login/', views.user_login, name='login' ),
    path('logout/', views.user_logout, name='logout' ),
    path('register_course/<str:nameCourse>/', views.register_course, name='register_course'),
    path('paymentFailed/<str:nameCourse>/', views.paymentFailed, name='paymentFailed'),
    path('paymentSuccessful/<str:nameCourse>/', views.paymentSuccessfull, name='paymentSuccessful'),
    path('profile/', views.profile, name='profile'),
]



