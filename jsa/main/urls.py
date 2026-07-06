from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("home", views.home),
    path("archive", views.archive),
    path("calendar", views.calendar),
    path("jcg", views.jcg),
    path("team", views.team),
]