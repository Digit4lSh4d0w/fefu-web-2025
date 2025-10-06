from django.urls import path

from fefu_lab import views

app_name = "fefu_lab"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("", views.IndexView.as_view(), name="home"),
    path("", views.IndexView.as_view(), name="about"),
    path("", views.IndexView.as_view(), name="students"),
]
