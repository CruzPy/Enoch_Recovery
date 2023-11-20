from django.shortcuts import render, redirect
from django.contrib import messages
from .models import OrientationRequest
from .forms import OrientationRequestForm
from .serializers import OrientationRequestSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .create_calendar_inv import create_calendar_inv
from .smtp import send_orientation_email


# Create your views here.
def home(request):
    return render(request, "index.html")


def testimonials(request):
    return render(request, "testimonials.html")


def locations(request):
    return render(request, "location.html")


def policy(request):
    return render(request, "policy.html")


def orientation(request):
    form = OrientationRequestForm()
    context = {
        "form": form,
    }
    return render(request, "orientation.html", context)


def submitted(request):
    if request.method == "POST":
        form = OrientationRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            # Check if an entry with the given email already exists
            if OrientationRequest.objects.filter(email=email).exists():
                # Entry already exists, show an error message
                messages.error(request, "Form has already been submitted.")
                return redirect("orientation")

            # Save the form to the database
            # form.save() # Enoch does not want to store user data

            cleaned_form = form.cleaned_data
            # Create google calendar inv
            google_link = create_calendar_inv(
                cleaned_form["date"],
                cleaned_form["time"],
                cleaned_form["location"],
            )

            # Send email notification to enoch and client
            send_orientation_email(cleaned_form, google_link)

            # Store vars into content
            content = {
                "form": form,
                "calendar_inv": google_link,
            }

            return render(request, "submitted.html", content)

        else:
            print("Form is invalid")
            messages.error(request, "Form is invalid. Please resubmit.")

    return redirect("orientation")


class OrientationRequestViewSet(viewsets.ModelViewSet):
    queryset = OrientationRequest.objects.all().order_by("date")
    serializer_class = OrientationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
