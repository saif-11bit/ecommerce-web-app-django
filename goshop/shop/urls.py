# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shophome"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="Contact us"),
    path('productView/<int:myid>', views.productView, name="Products"),
    path('tracker/', views.track, name="track"),
    path('search/', views.search, name="search"),
    path('checkout/', views.checkout, name="checkout"),
    path('pro_db/', views.pro_db, name="pro_db")
] 