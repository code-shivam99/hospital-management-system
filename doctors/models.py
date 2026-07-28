from django.db import models


class Doctor(models.Model):

    name = models.CharField(max_length=100)

    qualification = models.CharField(max_length=200)

    specialization = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    available_days = models.CharField(max_length=100)

    image = models.ImageField(upload_to='doctors/')

    def __str__(self):
        return self.name
