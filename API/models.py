from django.db import models

class studentModel(models.Model):
    name=models.CharField(max_length=50)
    Class=models.IntegerField()
    age= models.IntegerField()
    city=models.CharField(max_length=50)
    