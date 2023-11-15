from .models import OrientationRequest
from rest_framework import serializers

class OrientationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrientationRequest
        fields = "__all__"
    