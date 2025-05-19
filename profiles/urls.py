from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="index"),
    path("list", views.ProfileView.as_view(), name="profiles-list")
]
