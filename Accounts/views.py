from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from Accounts.forms import login_form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def AccountsLogin(request):
    form = login_form
    if request.method == "POST":
        # this means the request was ajax in nature
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"status": "authenticated"})
            else:
                return JsonResponse({"status": "invalid credentials"})
        else:   # this means the request was not ajax in nature
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("accounts:chk")
    else:
        form = login_form()

    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def AccountRegister(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("accounts:chk")
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def AccountsLogout(request):
    logout(request)
    return redirect("accounts:chk")


@login_required
def checkauth(request):
    return render(request, "authCheck.html")
