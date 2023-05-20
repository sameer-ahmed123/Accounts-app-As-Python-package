
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Accounts.views import AccountsLogin,checkauth,AccountRegister,AccountsLogout,chk2


app_name = "accounts"

urlpatterns = [
    path("authCheck",checkauth,name="authCheck"),
    path("login",AccountsLogin, name="login"),
    path("register",AccountRegister,name="register"),
    path("logout",AccountsLogout,name="logout"),
    path("check2",chk2,name="check2")
    
]
urlpatterns +=   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)