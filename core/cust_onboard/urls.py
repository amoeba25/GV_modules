from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show), # default route should be show
    path('create/', views.create), 
    path('edit/<slug:id>', views.edit), 
    path('update/<slug:id>', views.update), 
    path('delete/<slug:id>', views.destroy) 
]


