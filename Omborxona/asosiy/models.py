from django.db import models
from userapp.models import Omborxona
from django.core.validators import MinValueValidator
# Create your models here.

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    narx = models.IntegerField()
    son = models.IntegerField(validators=[MinValueValidator(1)])
    olchov = models.CharField(max_length=50,choices=(('dona','dona'),('kg','kg'),('litr','litr')))
    sana = models.DateField()
    omborxona = models.ForeignKey(Omborxona,on_delete=models.CASCADE)

    def __str__(self):
        return f"Mahsulot : {self.nom}, Brendi : {self.brend}"

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    dokon = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    manzil = models.CharField(max_length=100)
    omborxona = models.ForeignKey(Omborxona,on_delete=models.CASCADE)
    qarz = models.PositiveIntegerField(default=0,null=True)

    def __str__(self):
        return f"Mijoz : {self.ism}, Do'kon : {self.dokon}"