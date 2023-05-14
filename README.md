# Accounts App - Python Package

The **Accounts App** is an authentication package for Django that provides a simple and hassle-free way to create an authentication system in your Django projects. By installing this package, you can easily add user registration, login, and authentication functionality without the need to build it from scratch.

## Installation

To install the Accounts App package, you can use pip:

```shell
pip install accounts-app
```
## Usage

After installing the package, you can integrate it into your Django project by following these steps:

1. Add `'accounts'` to the `INSTALLED_APPS` list in your project's `settings.py` file:

   ```python
   INSTALLED_APPS = [
       # other apps
       'accounts',
   ]
   ```

2. Include the accounts URLs in your project's `urls.py` file:

    ```python
    from django.urls import include, path

    urlpatterns = [
        # other URL patterns
        path('accounts/', include('accounts.urls')),
    ]
    ```
    
3. Run migrations to create the necessary database tables:

```shell
python manage.py migrate
```   

4.Customize the main redirect URL in your project's `settings.py` file. This URL is where the login and register views will redirect users after successful authentication or registration.

```python
AUTH_REDIRECT_URL = '/dashboard/'
```
replace the '/dashboard/' with desired URL in your Project

5. Add context prcessor in your settings.py
```
python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                '**processors above **'
                'Accounts.context_processors.auth_url_redirect_processor', # add this line
            ],
        },
    },
]

```

## Features and Roadmap

The current version of the Accounts App provides the following features:

- User registration and login with username and password.
- Basic authentication using Django's User model.
- Extended forms (`UserCreationForm` and `AuthenticationForm`) for authentication.

The following features are planned for future versions:

- Google authentication.
- GitHub authentication.
- Facebook authentication.
- Password reset via email.
- Additional validation options and enhancements based on Django's authentication system.
- Option to log in with either email or username.

Please note that this project is currently a side project, and completion of the planned features may take some time. Additionally, there might be considerations to switch to a custom user model in the future, although this change has not been confirmed.
