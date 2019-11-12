from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    dict = {'name': 'This is dict'}
    return render(request, 'index.html', context=dict)


def about(request):
    return HttpResponse("This is my about page")


def contact(request):
    return HttpResponse("Contact us page")
