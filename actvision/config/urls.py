"""Actvision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home0
    .
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import loginapp.views
import home.views
import movie.views
import settings.views
import inform.views
import register.views
import imgn.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginapp.views.login, name='login.html'),
    path('login/', loginapp.views.login_success, name='login_success.html'),
    path('home', home.views.home, name='home.html'),
    path('home/movie', movie.views.movie, name='movie.html'),
    #path('home/setting', include('settings.urls')),
    path('home/setting', settings.views.settings, name='settings.html'),
    path('home/setting/update_Brightness', settings.views.update_Brightness, name='update_Brightness'),
    path('home/setting/update_min_max', settings.views.update_min_max, name='update_min_max'),
    path('home/setting/update_on_off', settings.views.update_on_off, name='update_on_off'),
    path('home/inform', inform.views.inform, name='inform.html'),
    path('home/register', register.views.register, name='register.html'),
    path('home/register/users_list', register.views.users_list, name='users_list'),
    path('home/imgn', imgn.views.imgn, name='image.html'),
    path('home/imgn/upload_img', imgn.views.upload_img, name='upload_img'),
]
