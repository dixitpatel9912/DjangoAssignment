from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.

def home(request):
    return render(request, 'index.html')


def form_view(request):
    form = forms.Loginform
    return render(request, 'forms.html', {'form': form})
