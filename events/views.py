from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

def booking(request):
    return render(request, 'booking.html')

def payment(request):
    return render(request, 'payment.html')
