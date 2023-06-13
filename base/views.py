from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.templatetags.static import static
import requests
from .models import Book


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
            description = volume_info.get('description')

            if title and authors:
                book = {
                    'title': title,
                    'authors': authors,
                    'image': image,
                    'description': description
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

def save_book(request):
    if request.method == 'POST':
        # Retrieve book information from the form data
        title = request.POST.get('title')
        authors = request.POST.get('authors')
        image = request.POST.get('image')
        description = request.POST.get('description')

        # Fetch additional book details from the Google Books API
        api_key = "YOUR_API_KEY"
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={title}&key={api_key}')
        data = response.json()

        if response.status_code == 200:
            items = data.get('items', [])
            if items:
                volume_info = items[0].get('volumeInfo', {})
                language = volume_info.get('language')
                category = volume_info.get('categories', [''])[0]  # Retrieve the first category if available

                # Create a new Book object and save it to the database
                book = Book(title=title, authors=authors, image=image, description=description, language=language, category=category)
                book.save()

                return redirect('book_list')

    return HttpResponse('Invalid request method.')

def your_view(request):
    books = Book.objects.all()  # Retrieve your book objects from the database
    context = {'books': books}
    return render(request, 'home.html', context)

def book_list(request):
    query = request.GET.get("book-name")
    api_key = "AIzaSyAr6_9amf0g0HAU5z8wP0jg2GwYtNX4g1k"
    books = []

    if query:
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}')
        data = response.json()

        if response.status_code == 200:
            for item in data.get('items', []):
                volume_info = item.get('volumeInfo', {})
                title = volume_info.get('title')
                authors = volume_info.get('authors')
                image_links = volume_info.get('imageLinks', {})
                image = image_links.get('thumbnail') if image_links else None
                description = volume_info.get('description')
                categories = volume_info.get('categories')
                language = volume_info.get('language')

                if title and authors:
                    book = {
                        'title': title,
                        'authors': authors,
                        'image': image,
                        'description': description,
                        'categories': categories,
                        'language': language,
                    }
                    books.append(book)

    saved_books = Book.objects.all()  

    context = {'books': books, 'saved_books': saved_books}
    return render(request, 'accounts/book_list.html', context)