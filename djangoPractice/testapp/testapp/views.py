from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def order(request):
    return render(request, 'order.html')