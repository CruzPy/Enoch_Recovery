from django.shortcuts import render, redirect
from .forms import OrientationRequestForm


# Create your views here.
def home(request):
    form = OrientationRequestForm()
    context = {
        "form": form,
    }
    return render(request, "index.html", context)


def testform(request):
    if request.method == "POST":
        form = OrientationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "submitted.html", {"form": form})

    else:
        form = OrientationRequestForm()
        return render(request, "testform.html", {"form": form})


def submitted(request):
    if request.method == "POST":
        form = OrientationRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save to DB
            return render(request, "submitted.html", {"form": form})

        else:
            print("Form is invalid")
        
    return redirect("home")  # Redirect to the home view if it's not a POST request
