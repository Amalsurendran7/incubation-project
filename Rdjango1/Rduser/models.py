from django.db import models
from django.contrib.auth.models import AbstractUser





class customer(models.Model):
    username=models.CharField(max_length=150,default=None,null=True)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    
    
    password=models.CharField(max_length=150)



# # Create your models here.
# class customer(AbstractUser):
#     username = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, unique=True)
#     phone=models.CharField(max_length=150)
#     password = models.CharField(max_length=255)
#     username = None

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []    