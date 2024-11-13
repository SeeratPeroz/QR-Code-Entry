from django.shortcuts import render, redirect
from .models import Patient, Entry
from .forms import PatientForm, EntryForm


def index(request):
    return render(request, 'index.html')


def entry_list(request):
    patients = Patient.objects.filter(is_active=False)
    print(patients)
    return render(request, "entry_list.html", {"patients": patients})


def add_patient(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        # Create and save a new Patient object
        Patient.objects.create(first_name=first_name, last_name=last_name, dob=dob)
        
        # Redirect to a success page or any other page
        return redirect('index')

    # Render the form page for GET request
    return render(request, 'index.html')

def activate_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.is_active = True
    patient.save()
    return redirect('entry_list')