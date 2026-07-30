from django.db import models
from datetime import datetime

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=120)
    Email=models.EmailField(max_length=120)
    password=models.CharField(max_length=100)
    dateTime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.Email}, {self.dateTime}'
    
"""
fname=Devanand
lname=Rai
mom=basanti
father=ramgrah
address=TIWARI+TOLA%2CBARI+GAV%2CGHUGHULI+BUZURG%2CMAHARAJGANJ
gender=male
state=Uttar+Pradesh
city=maharajganj
dob=2026-07-01
pincode=273151
course=btech
email=devanandrai3260%40gmail.com
"""
class testtable(models.Model):
    firstName=models.CharField(max_length=120)
    lastName=models.CharField(max_length=120)
    motherName=models.CharField(max_length=120)
    fatherName=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    gender=models.CharField(max_length=10)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    DateOfBirth=models.DateField()
    pincode=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    email=models.EmailField(blank=True, null=True)
    def __str__(self):
        return f'{self.firstName} {self.lastName} {self.state} {self.city}'
    
