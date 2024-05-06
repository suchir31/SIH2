from django.db import models

class frauddetect(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    followers=models.IntegerField()
    follows=models.IntegerField()
    descrpt=models.CharField(max_length=500)
    profile=models.CharField(max_length=10)
    private=models.CharField(max_length=10)
    