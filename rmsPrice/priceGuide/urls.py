from django.contrib import admin
from django.urls import path
from . import views
app_name = 'priceGuide'
urlpatterns = [
    #path('', views.index, name='index'), # 這裡的index是view裡的function
    path('', views.Home, name='home'),
    
]
