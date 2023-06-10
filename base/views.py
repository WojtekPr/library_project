from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
    return render(request, 'accounts/home.html')

def registerPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        print(uname,email,pass1,pass2)
    return render(request, 'accounts/register.html')

def loginPage(request):
    return render(request, 'accounts/login.html')