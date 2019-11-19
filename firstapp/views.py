from django.shortcuts import render , redirect
from django.http import HttpResponse
from . import forms


# Create your views here.

def home(request):
    return render(request, 'index.html')


def create(request):
    if request.method == "POST":
        form = forms.Login(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/success')
            except:
                print("error")
    else:
        form = forms.Login
    return render(request, 'form.html', {'form': form})

def success(request):
    return render(request,'success.html')
