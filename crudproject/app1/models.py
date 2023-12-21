from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.IntegerField(primary_key=True,max_length="10")
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=20)
    contact=models.IntegerField(max_length=10)