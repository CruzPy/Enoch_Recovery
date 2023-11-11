from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("contact/", views.contact, name="contact"),
    path("submitted/", views.submitted, name="submitted"),
]
