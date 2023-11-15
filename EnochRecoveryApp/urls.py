from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"orientation", views.OrientationRequestViewSet, basename='OrientationRequest')

urlpatterns = [
    path("", views.home, name="home"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("contact/", views.contact, name="contact"),
    path("submitted/", views.submitted, name="submitted"),
    
    # API
    path("api/", include(router.urls))
]
