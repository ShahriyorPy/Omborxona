from django.db import models
from asosiy.models import Mahsulot , Mijoz
from userapp.models import Omborxona
# Create your models here.

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    ombor = models.ForeignKey(Omborxona,on_delete=models.CASCADE)
    miqdor = models.IntegerField()
    olchov = models.CharField(max_length=150, choices=(('dona', 'dona'), ('kg', 'kg'), ('litr', 'litr')),null=True)
    sana = models.DateTimeField(auto_now_add=True)
    summa = models.IntegerField()
    tolangan_summa = models.IntegerField()
    nasiya = models.IntegerField()

    def save(self, *args,**kwargs):
        self.summa = int(self.miqdor) * int(self.mahsulot.narx)
        self.nasiya = int(self.summa) - int(self.tolangan_summa)
        super(Statistika, self).save(*args, **kwargs)
