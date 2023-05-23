from django.urls import path
from .views import Homepage, Register, Login, logoutuser, Register_ref

urlpatterns = [
    path('home/', Homepage, name="Home-page"),
    path('register/', Register, name="Register-page"),
    path('login/', Login, name="login-page"),
    path("logout/", logoutuser, name="logout"),
    path("register/<str:link>", Register_ref, name="Register-page")

]
