from django.shortcuts import render, redirect
from .models import Appointment
from doctors.models import Doctor


def book_appointment(request):

    doctors = Doctor.objects.all()

    if request.method == 'POST':

        patient_name = request.POST['patient_name']

        patient_email=request.POST['patient_email']

        doctor_id = request.POST['doctor']

        appointment_date = request.POST['appointment_date']

        problem = request.POST['problem']

        selected_doctor = Doctor.objects.get(id=doctor_id)

        Appointment.objects.create(

            patient_name=patient_name,

            patient_email=patient_email,

            doctor=selected_doctor,

            appointment_date=appointment_date,

            problem=problem

        )

        return redirect('/success/')

    return render(
        request,
        'appointments/book.html',
        {'doctors': doctors}
    )


def success(request):

    return render(
        request,
        'appointments/success.html'
    )
# for check appointment status
def check_appointment(request):

    appointment = None

    if request.method == 'POST':

        patient_email=request.user.email

        appointment = Appointment.objects.filter(
            patient_email=patient_email
        )

    return render(
        request,
        'appointments/check.html',
        {'appointment': appointment}
    )