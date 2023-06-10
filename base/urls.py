from django.urls import path
from . import views
from .views import registerPage, loginPage, HomePage


urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'), 
    path('home/', HomePage, name='home'),
]