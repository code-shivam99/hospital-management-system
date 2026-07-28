from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
    'doctor/<int:id>/',
    doctor_detail,
    name='doctor_detail'
    ),

    path(
    'all-doctors/',
    all_doctors,
    name='all_doctors'
),

]