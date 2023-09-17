from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Doctor, Patient, Appointment 
from django.db import IntegrityError

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()

    d = doctors.count()  # Count the number of doctors
    p = patients.count()  # Count the number of patients
    a = appointments.count()  # Count the number of appointments

    return render(request, 'Dashboard.html', {'d': d, 'p': p, 'a': a})

def Nav(request):
    return render(request, 'navigationbar.html')

def home(request):
    # if not request.user.is_staff:
    #     return redirect('login')
    return render(request, 'index.html')




def user_login_view(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard upon successful admin login
        else:
            error = 'yes'
    d = {'user': error}
    return render(request, 'login.html', d)


    
def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')





def view_doctor(request):
    if not request.user.is_staff:
        return redirect ('login')

    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)



def add_doctor(request):
    error = ""
    
    if request.method == "POST":
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n, mobile=c, special=sp)  # Use 'Doctor' instead of 'doctor'
            error = 'no'
        except IntegrityError:
            error = 'yes'
       
    d = {'error': error}
    return render(request, 'add_doctor.html', d)


def delete_doctor(request, pid):

    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')




def add_patient(request):
    error = ""
    
    if request.method == "POST":
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        d = request.POST['disease']
        add = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, Diseases=d, address=add)
            error = 'no'
        except IntegrityError:
            error = 'yes'
       
    d = {'error': error}
    return render(request, 'add_patient.html', d)

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')

    patients = Patient.objects.all()
    print(patients)  # Add this line to print the retrieved data
    
    d = {'patient': patients}
    return render(request, 'view_patient.html', d)


def delete_patient(request, pid):

    doctor = Patient.objects.get(id=pid)
    doctor.delete()
    return redirect('view_patient')


@login_required
def add_appointment(request):
    error = ""
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    if request.method == "POST":
        doctor_name = request.POST.get('doctor')
        patient_name = request.POST.get('patient')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Check if doctor_name and patient_name are not empty
        if doctor_name and patient_name:
            # Get doctor and patient objects based on their names
            doctor = Doctor.objects.filter(name=doctor_name).first()
            patient = Patient.objects.filter(name=patient_name).first()

            if doctor and patient:
                try:
                    Appointment.objects.create(doctor=doctor, patient=patient, date=date, time=time)
                    error = 'no'
                except IntegrityError:
                    error = 'yes'
            else:
                error = 'Invalid doctor or patient.'
        else:
            error = 'Doctor and patient names are required.'

    context = {
        'doctors': doctors,
        'patients': patients,
        'error': error,
    }
    return render(request, 'add_appointment.html', context)



@login_required

def view_appointment(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'view_appointment.html', context)

@login_required


def delete_appointment(request, pid):
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')
