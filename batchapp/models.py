from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    addres = models.TextField(max_length=100,null=True)
class Staff(models.Model):
    name=models.CharField(max_length=100)
    addres=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    # addres1=models.CharField(max_length=100,null=True)
class Student1(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()




