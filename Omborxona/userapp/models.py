from django.db import models
from django.contrib.auth.models import User

# userapp

# Create your models here.

class Omborxona(models.Model):
    nom = models.CharField(max_length=50)
    ism = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Omborxona : {self.nom}"

