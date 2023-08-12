from django.shortcuts import render, redirect
from .models import *
from django.views import View
from userapp.models import Omborxona
# Create your views here.

# def mahsulotlar(request):
#     if request.user.is_authenticated:
#         content = {
#             'mahsulotlar':Mahsulot.objects.filter(omborxona__user = request.user)
#         }
#         return render(request,'products.html',content)


class MahsulotlarView(View):
    def get(self, request):
        natija = Mahsulot.objects.filter(omborxona__user = request.user)
        qidiruv_sozi = request.GET.get('search')
        if qidiruv_sozi:
            natija = natija.filter(nom__contains=qidiruv_sozi)|natija.filter(brend__contains=qidiruv_sozi)
        content = {
            'mahsulotlar':natija,
            'omborxonas': Omborxona.objects.all()
        }
        return render(request,'products.html',content)

    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom = request.POST.get('pr_name'),
                brend = request.POST.get('pr_brand'),
                narx = request.POST.get('pr_price'),
                son = request.POST.get('pr_amount'),
                olchov = request.POST.get('olchov'),
                sana = request.POST.get('pr_sana'),
                omborxona = Omborxona.objects.get(user = request.user)
            )
            return redirect('/mahsulotlar/')


class MijozlarView(View):
    def get(self, request):
        natija = Mijoz.objects.filter(omborxona = Omborxona.objects.get(user = request.user))
        qidiruv_sozi = request.GET.get('search')
        if qidiruv_sozi:
            natija = natija.filter(ism__contains=qidiruv_sozi)|natija.filter(dokon__contains=qidiruv_sozi)
        content = {
            "mijozlar":natija,
            'omborxonas': Omborxona.objects.all()
        }
        return render(request,"clients.html",content)

    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                ism=request.POST.get('client_ism'),
                dokon = request.POST.get('client_dokon'),
                tel = request.POST.get('client_tel'),
                manzil = request.POST.get('client_manzil'),
                omborxona=Omborxona.objects.get(user=request.user)
            )
            return redirect('/clientlar/')
class DelProductView(View):
    def get(self, request, son):
        Mahsulot.objects.get(id = son).delete()
        return redirect('/mahsulotlar/')

class DelClientView(View):
    def get(self, request, son):
        Mijoz.objects.get(id = son).delete()
        return redirect('/clientlar/')

class UpdateMahsulotView(View):
    def get(self, request, son):
        content = {
            'mahsulot':Mahsulot.objects.get(id = son),
            'olchovlar':['dona','kg','litr']
        }
        return render(request,"product_update.html",content)
    def post(self, request, son):
        if request.user.is_authenticated:
            Mahsulot.objects.filter(id = son).update(
                narx=request.POST.get('pr_price'),
                son=request.POST.get('pr_amount'),
                olchov=request.POST.get('olchov'),
                sana=request.POST.get('pr_sana')
            )
            return redirect('/mahsulotlar/')
        return redirect('/')
class UpdateClientView(View):
    def get(self, request, son):
        content = {
            "client":Mijoz.objects.get(id=son)
        }
        return render(request,'client_update.html',content)
    def post(self, request, son):
        if request.user.is_authenticated:
            Mijoz.objects.filter(id=son).update(
                ism=request.POST.get('client_ism'),
                dokon = request.POST.get('client_dokon'),
                tel = request.POST.get('client_tel'),
                manzil = request.POST.get('client_manzil')
            )
            return redirect('/clientlar/')
        return redirect('/')

