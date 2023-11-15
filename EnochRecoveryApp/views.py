from django.shortcuts import render, redirect
from django.contrib import messages
from .models import OrientationRequest
from .forms import OrientationRequestForm
from .serializers import OrientationRequestSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .helper_functions import create_calendar_inv


# Create your views here.
def home(request):
    form = OrientationRequestForm()
    return render(request, "index.html")


def testimonials(request):
    return render(request, "testimonials.html")


def contact(request):
    form = OrientationRequestForm()
    context = {
        "form": form,
    }
    return render(request, "contact.html", context)


def submitted(request):
    if request.method == "POST":
        form = OrientationRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save to DB

            # Create google calendar inv
            google_link = create_calendar_inv(
                form.cleaned_data["date"],
                form.cleaned_data["time"],
                form.cleaned_data["location"],
            )

            content = {
                "form": form,
                "calendar_inv": google_link,
            }

            return render(request, "submitted.html", content)

        else:
            print("Form is invalid")
            messages.error(request, "Form is invalid. Please resubmit.")

            return redirect(
                "contact"
            )  # Redirect to the contact view if it's not a POST request


class OrientationRequestViewSet(viewsets.ModelViewSet):
    queryset = OrientationRequest.objects.all().order_by("date")
    serializer_class = OrientationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
