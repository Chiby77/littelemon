Little Lemon - Django REST API (Django + MySQL)

SETUP
  pipenv install
  pipenv shell
  # create MySQL database "littlelemon" and set credentials in littlelemon/settings.py
  python manage.py migrate
  python manage.py runserver
  python manage.py test

API PATHS TO TEST (base: http://127.0.0.1:8000)
  /api/menu/                  GET (public), POST (auth)
  /api/menu/<id>/             GET (public), PUT/PATCH/DELETE (auth)
  /api/bookings/              GET, POST (auth required)
  /api/bookings/<id>/         GET, PUT, PATCH, DELETE (auth required)
  /auth/users/                POST  {"username","password"}  -> register
  /auth/token/login/          POST  {"username","password"}  -> returns auth_token
  /auth/token/logout/         POST  (auth required)

AUTH HEADER (Insomnia)
  Authorization: Token <auth_token>

HTML PAGES
  /  /book/  /reservations/
