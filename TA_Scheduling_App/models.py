from django.db import models


# Create your models here.
class Account(models.Model):
    firstname = models.CharField(max_length=50, default='None')
    lastname = models.CharField(max_length=50, default='None')
    username = models.CharField(max_length=50, default='None')
    password = models.CharField(max_length=50, default='None')
    role = models.CharField(max_length=50, default='None')
    phone = models.CharField(max_length=50, default='None')
    email = models.CharField(max_length=50, default='None')
    address = models.CharField(max_length=50, default='None')
    course = models.CharField(max_length=50, default='None')
    lab = models.CharField(max_length=50, default='None')
    assignment = models.CharField(max_length=50, default='None')
    officehours = models.CharField(max_length=50, default='None')

class Lab(models.Model):
    lab = models.CharField(max_length=50, default='None')

class Instructor(models.Model):
    instructor = models.CharField(max_length=50, default='None')

class TA(models.Model):
    ta = models.CharField(max_length=50, default='None')

class Class(models.Model):
    course = models.CharField(max_length=50, default='None')
    labs = models.CharField(max_length=50, default='None')
    #labs = models.ForeignKey(Lab, on_delete=models.CASCADE, default='None')
    #labList = models.ListCharField(Lab)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default='None')
    ta = models.CharField(max_length=50, default='None')
    #ta = models.ForeignKey(TA, on_delete=models.CASCADE, default='None')
    #taList = models.ListCharField(Lab)

class Relationship(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, default='None')
    course = models.ForeignKey(Class, on_delete=models.CASCADE, default='None')
    labs = models.ForeignKey(Lab, on_delete=models.CASCADE, default='None')
