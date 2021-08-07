from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.EmailField()
    age = models.IntegerField()
    dob = models.DateTimeField()
    address = models.TextField()
    pincode = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    position = models.CharField(max_length=200)



    def _str__(self):
        return self.name 
    


