from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def AccountsLogin(request):
    form = AuthenticationForm
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request, user)
            return redirect("accounts:chk")
    else:
        form = AuthenticationForm()

    context = {
        "form":form,
    }
    return render(request, "login.html", context)

@login_required
def checkauth(request):
    return render(request,"authCheck.html")