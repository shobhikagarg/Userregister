from django.db import models

# Create your models here.
class Account(models.Model):
    email=models.EmailField(max_length=60,unique=True)
    firstname=models.CharField(max_length=50,null=True)
    lastname = models.CharField(max_length=50,null=True)
    passowrd1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)
    Favourite = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.email

class Userr(models.Model):
    email=models.EmailField(max_length=60,unique=True)
    user_id=models.IntegerField()
    password=models.CharField(max_length=10)
    login_type=models.CharField(max_length=20,default='signin')


    def __str__(self):
        return self.email

