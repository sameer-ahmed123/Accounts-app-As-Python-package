
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Accounts.views import AccountsLogin,checkauth,AccountRegister,AccountsLogout


app_name = "accounts"

urlpatterns = [
    path("authCheck",checkauth,name="chk"),
    path("login",AccountsLogin, name="login"),
    path("register",AccountRegister,name="register"),
    path("logout",AccountsLogout,name="logout"),
    
]
urlpatterns +=   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)