from django.db import models

# Create your models here.
class Accountcreate(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    phone=models.IntegerField()



    
