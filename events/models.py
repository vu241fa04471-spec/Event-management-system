from django.db import models
from django.contrib.auth.models import User

# Category Table
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Event Table
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    price = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Booking Table
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Payment Table
class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)

    amount = models.IntegerField()
    payment_status = models.CharField(max_length=100)

    def __str__(self):
        return self.payment_status