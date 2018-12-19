# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from django.core.validators  import RegexValidator
from django.utils.crypto import get_random_string

MALE = 'MA'
FEMALE = 'FE'
NA = 'NA'
ENABLED = 1
DISABLED = 0

GENDER_CHOICES = (
    (MALE, 'ผู้ชาย'),
    (FEMALE, 'ผู้หญิง'),
    (NA, 'ไม่ระบุ'),
)

IS_ENABLED = (
    (ENABLED,'แสดง'),
    (DISABLED,'ซ่อน')
)

class Customer(models.Model):

    name = models.CharField(max_length=100, help_text='customer full name', blank=False ,db_index=True)
    code = models.CharField(max_length=20, help_text='customer code', unique=True,db_index=True,validators=[RegexValidator(r'^C[0-9]{6}$',"รูปแบบรหัสลูกค้าไม่ถูกต้อง")])
    email = models.EmailField(max_length=100, help_text='email', blank=True, null=True, default=None, unique=True)
    birth_date = models.DateField(help_text='birthdate', blank=True,null=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=NA, help_text='gender')
    created_date = models.DateTimeField(auto_now_add=True, help_text='created date')
    mobile = models.CharField(max_length=20, help_text='customer mobile number', blank=True, null=True,validators=[RegexValidator(r'^0[0-9]{9}$','เบอร์มือถือไม่ถูกต้อง')], default=None, unique=True)
    is_enabled = models.IntegerField(default=ENABLED,choices=IS_ENABLED)
    secret = models.CharField(max_length=32,blank=True, null=True,validators=[RegexValidator(r'^[a-z0-9]{7}$','รูปแบบไม่ถูกต้อง')])
    user = models.OneToOneField(User, related_name='customer_user', on_delete=models.CASCADE)


class CustomerUser(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, related_name='customer', on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
