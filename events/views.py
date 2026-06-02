import django
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import Event, Registration

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')


def home(request):
    events = Event.objects.all()
    return render(request,'home.html',{'events':events})


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')

    else:
        form = RegisterForm()

    return render(request,'register.html',{'form':form})


@login_required
def register_event(request,event_id):

    event = Event.objects.get(id=event_id)

    Registration.objects.create(
        user=request.user,
        event=event
    )

    return redirect('myevents')


@login_required
def myevents(request):

    registrations = Registration.objects.filter(
        user=request.user
    )

    return render(
        request,
        'myevents.html',
        {'registrations':registrations}
    )


@login_required
def dashboard(request):

    context = {
        'events': Event.objects.count(),
        'users': Registration.objects.values('user').distinct().count(),
        'registrations': Registration.objects.count()
    }

    return render(request,'dashboard.html',context)

@login_required
def payment(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':

        Registration.objects.create(
            user=request.user,
            event=event,
            payment_status='Paid'
        )

        return redirect('booking_success')

    return render(
        request,
        'payment.html',
        {'event': event}
    )


def booking_success(request):
    return render(request, 'booking_success.html')

@login_required
def user_page(request):

    total_events = Registration.objects.filter(
        user=request.user
    ).count()

    context = {
        'total_events': total_events
    }

    return render(
        request,
        'user.html',
        context
    )