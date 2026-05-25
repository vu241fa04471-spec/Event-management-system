from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('booking/', views.booking, name='booking'),
    path('payment/', views.payment, name='payment'),
]