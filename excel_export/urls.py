"""excel_export URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import ListView

from .models import ExcelExport
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$',  views.demo_home, name = 'home'),
    url(r'^excel_export/$',  views.demo_details, name = 'demo_details'),
    url(r'^excel_export/(?P<pk>[0-9]+)/$',  views.demo_detail_id, name = 'demo_detail_id'),
    url(r'^excel_export/(?P<pk>[0-9]+)/edit/$',  views.demo_edit_id, name = 'demo_edit_id'),
    url(r'^excel_export/add/$',  views.demo_add, name = 'demo_add'),
    url(r'^excel_export/export/(?P<pk>[0-9]+)/$',  views.export_sig_to_excel, name = 'export_sig_to_excel'),
    url(r'^excel_export/exportall/$',  views.export_all_to_excel, name = 'export_all_to_excel'),
]
