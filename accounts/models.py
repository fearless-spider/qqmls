from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    # this is only required field
    user = models.OneToOneRel(User, 'id', 'user_id')
    user = models.OneToOneField(User)
    firstname = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)


class Address(models.Model):
    person = models.ManyToManyRel(Person, 'person_id')
    person = models.ManyToManyField(Person)
    address1 = models.CharField(max_length=55)
    address2 = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    zipcode = models.CharField(max_length=6)
    region = models.CharField(max_length=55)
    country = models.CharField(max_length=55)
