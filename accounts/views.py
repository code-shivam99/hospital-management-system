# from django.shortcuts import render

# def home(request):
#     return render( request,'home.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def register(request):

    if request.method == 'POST':

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        User.objects.create_user(

            username=username,

            email=email,

            password=password

        )

        return redirect('/login/')

    return render(
        request,
        'accounts/register.html'
    )


# login view
def user_login(request):

    message = ''


    # RESET SUCCESS POPUP

    reset_success = request.session.get(
        'password_reset_success',
        False
    )


    # POPUP ONLY ONCE

    if reset_success:

        request.session['password_reset_success'] = False



    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(

            request,

            username=username,

            password=password
        )


        if user is not None:

            login(request, user)

            return redirect('/')


        else:

            message = 'Invalid Username or Password'



    return render(

        request,

        'accounts/login.html',

        {

            'message': message,

            'reset_success': reset_success

        }
    )

# forgot password functionality
import random


otp_storage = {}


def forgot_password(request):

    if request.method == "POST":

        email = request.POST.get("email")

        try:

            User.objects.get(email=email)

            otp = random.randint(1000, 9999)

            otp_storage[email] = otp

            request.session['otp'] = otp

            return redirect(
                f"/reset-password/?email={email}"
            )

        except User.DoesNotExist:

            messages.error(
                request,
                "Email Not Found"
            )

    return render(
        request,
        "forgot_password.html"
    )

def reset_password(request):

    email = request.GET.get("email")

    otp = request.session.get('otp')


    if request.method == "POST":

        entered_otp = request.POST.get("otp")

        new_password = request.POST.get("password")


        if str(otp) == entered_otp:

            user = User.objects.get(email=email)

            user.set_password(new_password)

            user.save()


            # SUCCESS SESSION

            request.session['password_reset_success'] = True


            return redirect("/login/")


        else:

            messages.error(

                request,

                "Invalid OTP"

            )


    return render(

        request,

        "reset_password.html",

        {

            "otp": otp

        }
    )

# patient dashboard
from appointments.models import Appointment


@login_required
def dashboard(request):

    appointments = Appointment.objects.filter(
        patient_email=request.user.email
    )

    return render(
        request,
        'accounts/dashboard.html',
        {'appointments': appointments}
    )


# logout view
def user_logout(request):

    logout(request)

    return redirect('/')