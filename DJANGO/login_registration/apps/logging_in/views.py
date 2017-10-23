from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'logging_in/index.html')

def adduser(request):
    print('----------------ATTEMPTING ADD---------')
    errors = User.objects.validate_user(request.POST)
    print('----------------ADDED TO DB---------')
    if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
    else:
        user_id = User.objects.last().id
        return redirect('/logging_in/'+str(user_id)+'/success')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
    else:
        user_id = User.objects.filter(email = request.POST['email'])[0]
        print user_id
        return redirect('/logging_in/'+str(user_id.id)+'/success')

def success(request, user_id):
    user = {'user':User.objects.get(id=user_id)}
    return render(request, 'logging_in/success.html', user)
