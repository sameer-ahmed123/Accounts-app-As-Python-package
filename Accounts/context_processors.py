#add this to the package documentations 
from django.conf import settings

def auth_url_redirect_processor(request):
    auth_redirect_url = settings.AUTH_REDIRECT_URL
    return {
        "auth_redirect_url":auth_redirect_url
    }
    