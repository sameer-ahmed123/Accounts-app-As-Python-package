from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Accounts.forms import login_form, register_form
from django.conf import settings
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
                return redirect(settings.REDIRECT_VIEW_PACKAGE)
    else:
        form = login_form()

    context = {
        "form": form, #pass the settings.py redirect with context
    }
    return render(request, "login.html", context)


def AccountRegister(request):
    form = register_form
    if request.method == "POST":
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            print("AJAX Register")
            username = request.POST.get("username")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if (password1 == password2):
                print(username, password1, password2 + "in python view")
                # csn use the User model to create new user objects ??
                try:
                    user = User.objects.create_user(
                        username=username, password=password1)
                    # user.save()
                    login(request, user)
                    return JsonResponse({
                        "status": "success"
                    })
                except:
                    return JsonResponse({
                        "status": "fail"
                    })
            else:
                return JsonResponse({
                    "status": "password mismatch"
                })
        else:
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                login(request, user)

                return redirect(settings.REDIRECT_VIEW_PACKAGE)
    else:
        form = register_form()
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
