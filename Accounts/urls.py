from django.urls import path
from Accounts.views import AccountsLogin,checkauth


app_name = "accounts"

urlpatterns = [
    path("authCheck",checkauth,name="chk"),
    path("login",AccountsLogin, name="login"),
]