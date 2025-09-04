from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name='home'),
    path('/products',views.product, name='products'),
    path('/reservations',views.reservation, name='reservations'),
    path('/contact',views.contact, name='contact'),
    path('/about', views.about, name='about'),
]