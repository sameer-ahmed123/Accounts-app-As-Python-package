# Accounts-app-As-Python-package
an authntication package for django , to pip install and forget the hassel of creating a authentication system.


#working on:
making the redirect url dynamic for each project (in settings.py) ,
so when a new project installs this package it only has to change the main redirect url in settings.py 
(the "redirect url" in this case is the url to which the login and register view redirects after logging in /registering)


#TO DO:
1: add google auth
2: add github auth
3: add facebook auth
4: change password with email.
5: add all the validation to the auth package that is uesd by django to get a better understanding of how DJANGO handels all this 
6: add option to login with either email or Username 


#P.S
this is a side project so it may take a while to complete 
and this package utilizes the "User model" in django also it extends the "UserCeationForm" and the "AuthenticationForm" for all authentications 
might chage this to a Custom User model in future(Not Confirmed).
