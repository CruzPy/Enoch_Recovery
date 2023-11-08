from django.db import models
from phone_field import PhoneField


# Create your models here.
class OrientationRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = PhoneField(blank=True, help_text="Contact phone number")
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
