"""
URL configuration for scanner project.

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
from . import views

urlpatterns = [

    path('login/', views.scanner_login),
   # path('entry/<str:login_id>', views.entry_check),
    #path('exit/<str:login_id>', views.exit_check),
   # path('event/<str:token>/<str:login_id>', views.event_check),
    path('fetch_data/<str:date_time>/', views.get_qr),
]
