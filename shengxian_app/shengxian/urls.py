"""shengxian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from App import views
from App.admin import mysite

urlpatterns = [
    url('admin/', mysite.urls),

    # 直接访问主域名，直接派发到一个响应函数
    url('^$', views.index),

    # 以app/开头的请求派发到子路由表
    url('^app/', include('App.urls',namespace='app')),
]
