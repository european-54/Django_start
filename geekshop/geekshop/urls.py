"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from django.contrib import admin
#from django.conf.urls import path,include

from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, re_path
import mainapp.views as mainapp
#from geekshop.adminapp import views

app_name = 'mainapp'


def mainapp(args):
    pass


urlpatterns = [
    re_path(r'^$', mainapp, name='main'),
    re_path(r'^products/', include('mainapp.urls', namespace='products')),
    re_path(r'^order/', include('ordersapp.urls', namespace='order')),
    #path('admin/', admin.site.urls),
    path('products/', mainapp.products, name='product'),
    path('contact/', mainapp.contact, name='contact'),
    path('test/', mainapp.menu, name='menu'),
    path('', mainapp.main, name='main'),
    path('admin/', include('adminapp.urls', namespace='admin'))
]
