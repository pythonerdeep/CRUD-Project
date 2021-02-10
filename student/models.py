from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.CharField(max_length=20)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=20)
    semail=models.EmailField()
    scontact=models.CharField(max_length=15)
    def __str__(self):
        return self.semail

    class Meta():
        db_table="Student"