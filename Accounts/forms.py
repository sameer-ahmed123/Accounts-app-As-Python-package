from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "login_username ", "id": "id_username", "autofocus": True, "list": "id_usernames"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"autocomplete": "current-password", "class": "login_password", "autofocus": True}))


class register_form(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "password"}))
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "password"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(register_form, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        return user


