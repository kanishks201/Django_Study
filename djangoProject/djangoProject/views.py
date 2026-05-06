from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, World... Home page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, World... About page")

def contact(request):
    return HttpResponse("Hello, World... Contact page")