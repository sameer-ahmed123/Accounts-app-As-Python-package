from django import forms
from django.contrib.auth.forms import AuthenticationForm

class login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-lg ", "id": "id_username","autofocus": True,"list":"id_usernames"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete": "current-password","class": "form-control form-control-lg","autofocus": True}))