# --- Add to littlelemon/settings.py ---
INSTALLED_APPS += [
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "restaurant",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}

DJOSER = {"USER_ID_FIELD": "username"}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "littlelemon",
        "USER": "your_mysql_user",
        "PASSWORD": "your_mysql_password",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}

# --- littlelemon/urls.py ---
# from django.urls import path, include
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", include("restaurant.urls")),            # HTML pages (static content)
#     path("api/", include("restaurant.api_urls")),    # menu + bookings APIs
#     path("auth/", include("djoser.urls")),           # registration
#     path("auth/", include("djoser.urls.authtoken")), # token login/logout
# ]
