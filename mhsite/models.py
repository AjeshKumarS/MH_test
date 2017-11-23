# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models
import calendar

# Create your models here.
class Application(models.Model):
    admission_number=models.CharField(max_length=7,
                                    validators=[RegexValidator(regex=r'^[0-9]{4}/[0-9]{2}$',message='The format for admission number is 1234/17')],
                                    help_text='1234/17',unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    pincode=models.CharField(max_length=6,validators=[RegexValidator(regex=r'^[0-9]{6}$',message='Enter a valid pincode')])
    phone=models.CharField(max_length=10,validators=[RegexValidator(regex=r'[0-9]{10}',message='Invalid mobile number')])
    date_of_birth=models.DateField()
    distance=models.IntegerField(default=0)
    keam=models.IntegerField(default=0,verbose_name="KEAM Mark")
    plus_2=models.DecimalField(default=00.00,max_digits=4,decimal_places=2,verbose_name="% of Mark Obtained in +2")
    category=models.CharField(max_length=10)
    religion=models.CharField(max_length=50)
    caste=models.CharField(max_length=50)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Profile(models.Model):
    pass


class Expense(models.Model):
    #MONTH_CHOICES=[(str(i), calendar.month_name[i]) for i in range(1,13)]

    #month=models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
    date=models.DateField(unique=True)
    item1=models.DecimalField(default=0.0,decimal_places=2,max_digits=10)
    item2=models.DecimalField(default=0.0,decimal_places=2,max_digits=10)
    item3=models.DecimalField(default=0.0,decimal_places=2,max_digits=10)
    item4=models.DecimalField(default=0.0,decimal_places=2,max_digits=10)
    item5=models.DecimalField(default=0.0,decimal_places=2,max_digits=10)

    @property
    def total(self):
        "Return the total expense"
        sum=0
        sum+=(self.item1+self.item2+self.item3+self.item4+self.item5)
        return sum
    total_expense=property(total)

    def __str__(self):
        return str(self.date)

class MessCut(models.Model):
    email=models.EmailField(unique=True)
    mess_cut_dates=models.CharField(max_length=100000)

    def __str__(self):
        return self.email
