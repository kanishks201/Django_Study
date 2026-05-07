from django.shortcuts import render

# Create your views here.


def all_chai(request):
    return render(request, 'djangoApp/all_djangoApp.html')