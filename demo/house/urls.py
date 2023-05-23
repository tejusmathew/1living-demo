from .import views
from django.urls import path


urlpatterns = [
    path("form/", views.form, name="form"),
    path("", views.home, name="home"),
    path("refer", views.link, name="referal name"),
    #path("link/", views.unq, name="link display")
    path("refer/<str:link>", views.name, name="link display")
]
