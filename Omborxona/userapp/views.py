from django.shortcuts import render,redirect
from asosiy.models import Mahsulot
from userapp.models import Omborxona
from django.contrib.auth import authenticate,login,logout
from django.views import View
# Create your views here.

# def bulimlar(request):
#     if request.user.is_authenticated:
#         return render(request,'bulimlar.html')

class BulimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request,'bulimlar.html')
        return redirect('/')

# def login_view(request):
#     if request.method == 'POST':
#         user =authenticate(
#             username = request.POST.get('l'),
#             password = request.POST.get('p')
#         )
#         if user is not None:
#             login(request,user)
#             return redirect('/bulimlar/')
#         return redirect('/')
#     return render(request, 'home.html')

class Login_viewView(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        user = authenticate(
                username = request.POST.get('l'),
                password = request.POST.get('p')
                )
        if user is not None:
            login(request,user)
            return redirect('/bulimlar/')
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')

