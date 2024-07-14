from django.urls import path

from . import views

urlpatterns = [
    path("articles/", views.special_case_2003),
]