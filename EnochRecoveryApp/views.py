from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, "index.html")


def submitted(request):
    if request.method == "POST":
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        location = request.POST.get("location")

        context = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "date": date,
            "time": time,
            "location": location,
        }
        return render(request, "submitted.html", context)

    else:
        return redirect("home")  # Redirect to the home view if it's not a POST request
