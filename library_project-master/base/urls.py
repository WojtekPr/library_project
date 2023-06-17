from django.urls import path
from . import views
# from .views import registerPage, loginPage, HomePage, registeredPage


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'), 
    path('registered/', views.registeredPage, name='registered'), 
    path('home/', views.HomePage, name='home'),
    path('logout/', views.logoutPage, name='logout'),
    path('save_book/', views.save_book, name='save_book'),
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),
    path('books/', views.book_list, name='book_list'),

]