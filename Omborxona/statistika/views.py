from django.shortcuts import render, redirect
from .models import *
from userapp.models import Omborxona
from asosiy.models import Mijoz,Mahsulot
from django.views import View
# Create your views here.

class StatsView(View):
    def get(self, request):
        natija = Statistika.objects.filter(ombor__user = request.user)
        qidiruv_sozi = request.GET.get('search')
        if qidiruv_sozi:
            natija = natija.filter(mahsulot__nom__contains=qidiruv_sozi)|natija.filter(mijoz__ism__contains=qidiruv_sozi)|natija.filter(
                mijoz__dokon__contains=qidiruv_sozi)
        content = {
            'stats':natija,
            'mijozlar':Mijoz.objects.filter(omborxona__user=request.user),
            'mahsulotlar':Mahsulot.objects.filter(omborxona__user=request.user)
        }
        return render(request,'stats.html',content)

    def post(self, request):
        if request.user.is_authenticated:
            Statistika.objects.create(
                mahsulot=Mahsulot.objects.get(id=request.POST.get('mahsulot')),
                mijoz = Mijoz.objects.get(id=request.POST.get('client')),
                ombor = Omborxona.objects.get(user = request.user),
                miqdor = request.POST.get('miqdor'),
                olchov = request.POST.get('olchov'),
                sana = request.POST.get('sana'),
                summa = request.POST.get('summa'),
                tolangan_summa = request.POST.get('tolandi'),
                nasiya = request.POST.get('nasiya')
            )
            # Avtomatlashtirish:
            mijoz = Mijoz.objects.get(id=request.POST.get('client'))
            mijoz.qarz+= int(request.POST.get('nasiya'))
            mijoz.save()

            mahsulot = Mahsulot.objects.get(id=request.POST.get('mahsulot'))
            mahsulot.son -= int(request.POST.get('miqdor'))
            mahsulot.save()
            return redirect('/stats/')

class DelStatView(View):
    def get(self, request, son):
        Statistika.objects.get(id = son).delete()
        return redirect('/stats/')