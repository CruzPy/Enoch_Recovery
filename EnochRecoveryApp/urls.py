from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("submitted/", views.submitted, name="submitted"),
    path("testform/", views.testform, name="testform"),
]
