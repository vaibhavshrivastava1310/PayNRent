from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=200, blank=False, default='')
    description= models.CharField(max_length=200,blank=False, default='')
    icon = models.ImageField(upload_to='static/') # after every change use python manage.py makemigrations then python manage.py migrate in terminal
class SubCategory(models.Model):
    categoryid = models.CharField(max_length=200, blank=False, default='')
    companyname= models.CharField(max_length=200,blank=False, default='')
    subcategoryname=models.CharField(max_length=200,blank=False, default='')
    description=models.CharField(max_length=200,blank=False, default='')
    icon = models.ImageField(upload_to='static/')
class Vehicles(models.Model):
    categoryid = models.CharField(max_length=200, blank=False, default='')
    subcategoryid = models.CharField(max_length=200, blank=False, default='')
    companyname= models.CharField(max_length=200,blank=False, default='')
    variant=models.CharField(max_length=200,blank=False, default='')
    modelyear = models.CharField(max_length=200, blank=False, default='')
    price = models.CharField(max_length=200, blank=False, default='')
    insured = models.CharField(max_length=200, blank=False, default='')
    registrationno = models.CharField(max_length=200, blank=False, default='')
    ownername = models.CharField(max_length=200, blank=False, default='')
    mobileno=models.CharField(max_length=200,blank=False, default='')
    color=models.CharField(max_length=200,blank=False, default='')
    fueltype = models.CharField(max_length=200, blank=False, default='')
    noofseats = models.CharField(max_length=200, blank=False, default='')
    transmissiontype = models.CharField(max_length=200, blank=False, default='')
    picture = models.ImageField(upload_to='static/')
class Administrator(models.Model):
    adminname = models.CharField(max_length=200, blank=False, default='')
    mobileno= models.CharField(max_length=200,blank=False, default='')
    emailid = models.CharField(max_length=200,blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
