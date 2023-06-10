from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
    context  = {}
    return render(request, 'accounts/home.html', context)

def registerPage(request):
    context = {}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)