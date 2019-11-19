from django import forms
from django.core import validators
from .models import Update_data


class Login(forms.ModelForm):
    class Meta:
        model = Update_data
        fields = "__all__"


'''

def check(value):
    if value[0].lower != 'a':
        raise forms.ValidationError('The name should start with a')


class Loginform(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=50)
    email = forms.EmailField(max_length=50)
    verify_email= forms.EmailField(max_length=50,label='Re-enter your email')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
    password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(4)])

    def clean(self):
        email=self.cleaned_data['email']
        vmail=self.cleaned_data['verify_email']
        if email!=vmail:
            raise forms.ValidationError("your email doesnt match")

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError('Provide atleast 4 characters')
        return password

'''
