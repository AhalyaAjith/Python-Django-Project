from django.db import models
import datetime
from django.contrib.auth import get_user_model
# Create your models here.

class Login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.TextField()
    Usertype=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_login'

class UserRegister(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(Login, on_delete=models.CASCADE)
    Name=models.CharField(max_length=50, null=True)
    phone_number=models.BigIntegerField(null=True)
    Email=models.CharField(max_length=50)
    Address=models.TextField()
    class Meta:
        db_table='tbl_user_register' 

class Laundry_package(models.Model):
    l_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    class Meta:
        db_table = 'tbl_laundry_package'


class Booking(models.Model):
    b_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    package = models.ForeignKey(Laundry_package, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    status = models.CharField(max_length=50)
    class Meta:
        db_table = 'tbl_booking'

class Feedback(models.Model):
    fd_id = models.AutoField(primary_key=True)  
    date = models.DateTimeField(auto_now_add=True) 
    feedback = models.TextField() 
    reply = models.TextField(blank=True, null=True)  
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE) 

    class Meta:
        db_table = 'tbl_feedback'

    