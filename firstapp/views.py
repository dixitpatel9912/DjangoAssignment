from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.

def home(request):
    return render(request, 'index.html')


def form_view(request):
    form = forms.Loginform
    if request.method == "POST":
        form = forms.Loginform(request.POST)
        if form.is_valid():
            print("Validations worked")
            print("Name:" + form.cleaned_data['name'])
            print("Email_id:" + form.cleaned_data['email'])
            print("password:" + form.cleaned_data['password'])
            print("verified_email:" + form.cleaned_data['verify_email'])
    return render(request, 'forms.html', {'form': form})
