"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'career_find'

urlpatterns = [
    path('', views.index , name = 'index'),
    url(r'result/(?P<page_num>\d+)/', views.result , name = 'result'),
    url(r'result/(?P<check_box>.+)/(?P<page_num>\d+)/', views.page , name = 'page')
    # url(r'no_req/(?P<page_num>\d+)/', no_req , name = 'no_req')
]