from django.shortcuts import render, redirect
from .forms import OrientationRequestForm


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
            return render(request, "submitted.html", {"form": form})

        else:
            print("Form is invalid")

    return redirect("contact")  # Redirect to the contact view if it's not a POST request
