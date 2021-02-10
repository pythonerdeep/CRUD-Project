from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class Registration(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=15,unique=True)
    mobile=models.IntegerField()

    def __str__(self):
        return self.username