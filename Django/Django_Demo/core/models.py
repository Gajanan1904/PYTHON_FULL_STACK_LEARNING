from django.db import models

# Create your models here.

# Django database model
class Product(models.Model):
    # Creating table named Product
    name = models.CharField(max_length=50)
    price = models.IntegerField()

# This creates database table blueprint
# Why we are doing this:
# Backend needs to store data permanently
# Without model -> no database -> no real backend
