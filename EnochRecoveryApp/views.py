from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

def submitted(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        cell = request.POST.get('cell')
        date = request.POST.get('date')
        appt = request.POST.get('appt')

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'cell': cell,
            'date': date,
            'appt': appt,
        }
        return render(request, 'submitted.html', context)
    return redirect('home')  # Redirect to the home view if it's not a POST request