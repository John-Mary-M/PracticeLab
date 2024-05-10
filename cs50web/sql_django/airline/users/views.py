from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    '''Displays information about the currently signed in user'''
    # check if user is signed in or not
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login_view'))
    return render(request, 'users/user.html')

def login_view(request):
    '''Validates user and logs in'''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid Credentials'
            })

    return render(request, 'users/login.html')

def logout_view(request):
    '''logs out a user'''
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Logged Out!✔️'
    })