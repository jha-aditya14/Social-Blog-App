from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    # first_name= models.CharField(max_length=100, default='NA')
    img=models.ImageField(upload_to='pics', null=True)
    # contact = models.BigIntegerField(null=True)
    username = None
    email= models.EmailField(unique=True, max_length=200)
    # password= models.CharField(max_length=100, default='NA')
    # createdAt=models.DateTimeField(null=False)
    updatedAt = models.DateTimeField(null=True)
    # lastLogin = models.DateTimeField(null=True)
    # last_name=models.CharField(max_length=100)
    objects= UserManager()
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
