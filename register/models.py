from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length = 30,unique=True)
    email = models.EmailField(max_length = 30,unique=True)
    phoneno = models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    date_time=models.DateTimeField(null=True)



class Messages(models.Model):
	sender=models.CharField(max_length=30,unique=False)
	receiver= models.CharField(max_length = 30,unique=False)
	message=models.CharField(max_length=100000)
	date_time=models.DateTimeField(default="0")
	time=models.CharField(max_length=20,unique=False,default=0)



    

