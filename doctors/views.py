from django.shortcuts import render
from .models import Doctor

def home(request):

    doctors = Doctor.objects.all()[:4]

    return render(

        request,

        'home.html',

        {'doctors': doctors}

    )

def all_doctors(request):

    doctors = Doctor.objects.all()

    return render(

        request,

        'all_doctors.html',

        {'doctors': doctors}

    )


def doctor_detail(request, id):

    doctor = Doctor.objects.get(id=id)

    return render(

        request,

        'doctor_detail.html',

        {'doctor': doctor}

    )