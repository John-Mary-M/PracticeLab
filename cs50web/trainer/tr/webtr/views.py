from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def home(request):
    '''Renders home page'''
    return render(request, 'webtr/home.html')

def todos(request):
    '''renders a list of todos with their status'''
    items = TodoItem.objects.all()
    return render(request, 'webtr/todos.html',{
        'todos': items
    })