from django import forms


class Loginform(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=50)
    email = forms.EmailField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)
