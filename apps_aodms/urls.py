from django.contrib import admin
from django.urls import path,include
from Rmsstores import models
from apps_aodms import views as v1
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',v1.login),
    path('apps/',v1.apps),
    path('apps/Rmsstores/',include('Rmsstores.urls')),
    path('apps/logout',v1.logout)
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

