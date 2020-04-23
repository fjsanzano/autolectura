"""MiReserva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path

from apps.lectura.views import MeterReadingList, MeterReadingCreate, MeterReadingDelete

urlpatterns = [
    path('', MeterReadingList.as_view(), name='read-list'),
    path('add/', MeterReadingCreate.as_view(), name='read-add'),
    # path('<int:pk>/', MeterReadingUpdate.as_view(), name='read-update'),
    path('<int:pk>/delete/', MeterReadingDelete.as_view(), name='read-delete'),
]
