from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Book
# Create your views here.
def index(request):
    print('---------------ENTERING INDEX--------------')
    return render(request, 'bookreviewer/index.html')

def process_adduser(request, methods=['POST']):
    print('---------------ATTEMPTING ADD--------------')
    errors = User.objects.user_manager(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        print('---------------ADDED TO DB--------------')
        user_id = User.objects.last().id
        return redirect('/')

def process_login(request, methods=['POST']):
    print('------------------ATTEMPTING LOGIN------------')
    errors = User.objects.login_validator(request.POST)
    print(errors)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['email'])
        print user
        request.session['user_id'] = user.id
        print('--------------ATTEMPTING REDIRECT TO BOOKS------------------')
        return redirect('/books')

def books(request, user):
    print('---------------ENTERING HOMEPAGE-------(BOOKS)-------')
    all_books = { 'all_books' : Book.objects.all().values() }
    # print(User.objects.get(id=user_id)
    # user = {'user':User.objects.get(id=user_id)}
    return render(request, 'bookreviewer/books.html', context=all_books)

def addnew(request):
    print('---------------ENTERING ADDBOOK--------------')
    return render(request, 'bookreviewer/addnew.html')

def process_addbook(request, methods=['POST']):
    print('---------------ATTEMPTING ADD--------------')
    errors = Book.objects.book_manager(request.POST)
    # if len(errors):
    #     for tag, error in errors.iteritems():
    #         messages.error(request, error, extra_tags=tag)
    #     return redirect('addnew')
    Book.objects.create(title=request.POST['title'], author=request.POST['author'], review=request.POST['review'])
    print('---------------ADDED TO DB--------------')
    return redirect('books')
