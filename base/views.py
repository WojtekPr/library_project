from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.templatetags.static import static
import requests


def HomePage(request):
    context = {}  
    api_key = "AIzaSyAr6_9amf0g0HAU5z8wP0jg2GwYtNX4g1k"
    query = request.GET.get("book-name")
    response=requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}')
    data = response.json()
    
    if response.status_code == 200:
        data = response.json()
        books = []

        # Extract book titles
        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title')
            authors = volume_info.get('authors')
            image_links = volume_info.get('imageLinks', {})
            image = image_links.get('thumbnail') if image_links else None

            if title and authors:
                book = {
                    'title': title,
                    'authors': authors,
                    'image': image
                }
                books.append(book)

        context = {'books': books}

    return render(request, 'accounts/home.html',context)

def registerPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Podane hasła nie są zgodne")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('registered')
        


    return render(request, 'accounts/register.html')


def registeredPage(request):
    return render(request, 'accounts/registered.html')

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Login lub hasło niepoprawne")
    return render(request, 'accounts/login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')