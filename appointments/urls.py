from django.urls import path
from .views import *

urlpatterns = [

    path(
        'book-appointment/',
        book_appointment,
        name='book_appointment'
    ),

    path(
        'success/',
        success,
        name='success'
    ),
    # for check appointment status
    path(
    'check-appointment/',
    check_appointment,
    name='check_appointment'
),

]

