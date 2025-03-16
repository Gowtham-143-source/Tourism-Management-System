from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .forms import DestinationForm

# List of destinations
def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/destination_list.html', {'destinations': destinations})

# Create a new destination
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm()
    return render(request, 'destinations/destination_form.html', {'form': form})

# Update a destination
def destination_update(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'destinations/destination_form.html', {'form': form})

# Delete a destination
def destination_delete(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destination.delete()
        return redirect('destination_list')
    return render(request, 'destinations/destination_confirm_delete.html', {'destination': destination})

