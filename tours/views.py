from django.shortcuts import render, redirect
from .models import TourPackage
from .forms import BookingForm



def packages(request):
    return render(request, 'tours/packages.html')

def intern1(request):
    return render(request, 'tours/Intern1.html')

def universe1(request):
    return render(request, 'tours/Universe1.html')

def family1(request):
    return render(request, 'tours/Family1.html')

def table(request):
    return render(request, 'tours/Table.html')

def form(request):
    return render(request, 'tours/form.html')

def packages(request):
    tours = TourPackage.objects.all()
    return render(request, 'tours/packages.html', {'tours': tours})

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('packages')  # Redirect to packages page after booking
    else:
        form = BookingForm()
    return render(request, 'tours/form.html', {'form': form})

# Create your views here.
