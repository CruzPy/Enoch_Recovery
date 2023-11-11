from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("submitted/", views.submitted, name="submitted"),
]
