from django.db import models
from doctors.models import Doctor


class Appointment(models.Model):

    patient_name = models.CharField(max_length=100)

    patient_email = models.EmailField()

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    problem = models.TextField()

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    STATUS_CHOICES = [

        ('Pending', 'Pending'),

        ('Approved', 'Approved'),

        ('Rejected', 'Rejected'),

    ]


    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='Pending'

    )

    def __str__(self):
        return self.patient_name