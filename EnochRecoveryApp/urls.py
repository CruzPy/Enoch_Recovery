from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(
    r"orientation", views.OrientationRequestViewSet, basename="OrientationRequest"
)

urlpatterns = [
    path("", views.home, name="home"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("locations/", views.locations, name="locations"),
    path("orientation/", views.orientation, name="orientation"),
    path("submitted/", views.submitted, name="submitted"),
    path("privacy-policy/", views.policy, name="policy"),
    # API
    path("api/", include(router.urls)),
]
