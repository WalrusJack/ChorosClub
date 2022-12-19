from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Place, Trip, Log
from .forms import UserProfileForm, TripForm, LogForm


# Create your views here.
def index(request):
    search_term = request.GET.get('search-term') or ''
    user_profiles = UserProfile.objects.filter(user__username__icontains=search_term)
    context = {'user_profiles': user_profiles}
    return render(request, 'index.html', context)


def sign_up(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            UserProfile.objects.create(user=user)
            return redirect('home')
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'sign_up.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def profile(request, username):
    user = User.objects.get(username=username)
    user_profile = user.profile
    trips = Trip.objects.filter(user=user)
    logs = Log.objects.filter(user=user)
    context = {'trips': trips, 'logs': logs, 'user_profile': user_profile}
    return render(request, 'profile.html', context)


@login_required
def new_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Trip.objects.create(user=request.user, title=title, description=description)
            return redirect('profile', request.user)
    form = TripForm()
    edit = False
    context = {'form': form, 'edit': edit}
    return render(request, 'new_trip.html', context)


@login_required
def new_log(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            log_type = form.cleaned_data['type']
            place = Place.objects.create(name=request.POST.get('place'))
            trip = form.cleaned_data['trip']
            Log.objects.create(user=request.user, title=title, description=description, type=log_type,
                               place=place, trip=trip)
            return redirect('profile', request.user)
    form = LogForm()
    edit = False
    context = {'user': request.user, 'form': form, 'edit': edit}
    return render(request, 'new_log.html', context)


@login_required
def new_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            UserProfile.objects.create(user=request.user, bio=bio)
            return redirect('profile', request.user)
    form = UserProfileForm()
    context = {'form': form}
    return render(request, 'new_profile.html', context)


@login_required
def edit_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    if request.method == 'POST':
        form = TripForm(request.POST or None, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user)
    form = TripForm(instance=trip)
    edit = True
    context = {'form': form, 'edit': edit, 'trip_id': trip_id}
    return render(request, 'new_trip.html', context)


@login_required
def edit_profile(request, profile_id):
    user_profile = UserProfile.objects.get(id=profile_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST or None, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user)
    form = UserProfileForm(instance=user_profile)
    context = {'form': form, 'profile_id': profile_id}
    return render(request, 'new_profile.html', context)


@login_required
def edit_log(request, log_id):
    log = Log.objects.get(id=log_id)
    if request.method == 'POST':
        form = LogForm(request.POST or None, instance=log)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user)
    form = LogForm(instance=log)
    edit = True
    context = {'form': form, 'edit': edit, 'log_id': log_id}
    return render(request, 'new_log.html', context)


@login_required
def delete_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip.delete()
    return redirect('profile', request.user)


@login_required
def delete_log(request, log_id):
    log = Log.objects.get(id=log_id)
    log.delete()
    return redirect('profile', request.user)
