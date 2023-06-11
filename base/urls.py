from django.urls import path
from . import views
# from .views import registerPage, loginPage, HomePage, registeredPage


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'), 
    path('registered/', views.registeredPage, name='registered'), 
    path('home/', views.HomePage, name='home'),
    path('logout/', views.logoutPage, name='logout'),

]