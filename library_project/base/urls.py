from django.urls import path
from . import views
from .views import registerPage, loginPage


urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),

]