from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
#Create your models here.

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=30,null=True)
    lastName = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=12 ,null=True)
    address=models.CharField(max_length=100,null=True)
    image = models.ImageField(default="logo-2.png",upload_to='users/', null=True, blank=True )

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Noticee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='noticee_user')
    issue_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='noticee')
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=700)
    file = models.FileField(upload_to='notice_files', blank=True)

    def __str__(self):
           return self.name


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='request_user')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='requests')
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=700)
    issue_date = models.DateField(blank=True, null=True)
    noted = models.NullBooleanField(default=False)
    file = models.FileField(upload_to='notice_files', blank=True)

    def __str__(self):
           return self.name

