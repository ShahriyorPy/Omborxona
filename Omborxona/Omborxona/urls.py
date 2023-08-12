"""
URL configuration for Omborxona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from userapp.views import *
from asosiy.views import *
from statistika.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bulimlar/',BulimlarView.as_view()),
    path('',Login_viewView.as_view()),
    path('logout/',logout_view),
    path('mahsulotlar/',MahsulotlarView.as_view()),
    path('clientlar/',MijozlarView.as_view()),
    path('del_product/<int:son>/',DelProductView.as_view()),
    path('del_stat/<int:son>/',DelStatView.as_view()),
    path('del_client/<int:son>/',DelClientView.as_view()),
    path('update_mahsulot/<int:son>/',UpdateMahsulotView.as_view()),
    path('update_client/<int:son>/',UpdateClientView.as_view()),
    path('stats/', StatsView.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
