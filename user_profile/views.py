from .forms import UserLoginForm, UserRegisterForm
from .models import Booking, Payment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
import json

# Create your views here.


def home(request):
    login_form = UserLoginForm
    register_form = UserRegisterForm
    context = {
        'login_form': login_form,
        'register_form': register_form,
        'active': 'login_form'
    }
    return render(request, 'index.html', context=context)


@ensure_csrf_cookie
def user_login(request):
    login_form = UserLoginForm(request.POST or None)
    register_form = UserRegisterForm()
    if login_form.is_valid():
        user = authenticate(username=login_form.cleaned_data.get('username'),
                            password=login_form.cleaned_data.get('password'))
        login(request, user)
        return redirect('/user_profile/')
    context = {
        'login_form': login_form,
        'register_form': register_form,
        'active': 'login_form'
    }
    return render(request, 'index.html', context=context)


@ensure_csrf_cookie
def user_register(request):
    login_form = UserLoginForm()
    register_form = UserRegisterForm(request.POST or None)
    if register_form.is_valid():
        user = register_form.save(commit=False)
        password = register_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        user = authenticate(username=user.username,
                            password=password)
        login(request, user)
        return redirect('/user_profile/')
    context = {
        'login_form': login_form,
        'register_form': register_form,
        'active': 'register_form'
    }
    return render(request, 'index.html', context=context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def user_profile(request):
    context = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name
    }
    return render(request, 'user_profile.html', context=context)


@login_required
def show_bookings(request):
    all_bookings = dict()
    bookings = Booking.objects.all()

    for booking in bookings:
        payments = Payment.objects.filter(booking=booking)
        all_bookings[booking.name] = []
        for payment in payments:
            all_bookings[booking.name].append(payment.fair_amount)
    print (json.dumps(all_bookings,indent=4))
    context = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'bookings': all_bookings
    }
    return render(request, 'user_profile.html', context=context)
