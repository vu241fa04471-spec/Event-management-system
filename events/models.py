from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    payment_status = models.CharField(
        max_length=20,
        default='Pending'
    )

    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username