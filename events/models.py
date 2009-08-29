from django.db import models
from django.contrib.auth.models import User
from qqmls.accounts.models import Person, Address


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    register_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User)
    person = models.ForeignKey(Person)
    address = models.ManyToManyRel(Address, 'address_id')
    address = models.ManyToManyField(Address)
    status = models.IntegerField()


class Agenda(models.Model):
    title = models.CharField(max_length=255)
    descriptiom = models.TextField()
    event_day = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    event = models.ForeignKey(Event)
