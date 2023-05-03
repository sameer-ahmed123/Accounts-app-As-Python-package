from django.urls import path
from Accounts.views import AccountsLogin,checkauth,AccountRegister


app_name = "accounts"

urlpatterns = [
    path("authCheck",checkauth,name="chk"),
    path("login",AccountsLogin, name="login"),
    path("register",AccountRegister,name="register"),
]