from django.db import models


# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    lab = models.CharField(max_length=50)
    assignment = models.CharField(max_length=50)


class Account(models.Model):
    account = models.ForeignKey(Person, on_delete=models.CASCADE)
