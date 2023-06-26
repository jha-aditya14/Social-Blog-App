from django.db import models
from blogHome.models import User
# Create your models here.

class Blogs(models.Model):
    blogName = models.CharField(max_length=300)
    Description = models.CharField(max_length=1500)
    img=models.ImageField(upload_to='blogPics' , null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt=models.DateTimeField(null=False)
    updatedAt = models.DateTimeField(null=True)