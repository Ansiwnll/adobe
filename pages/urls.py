from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('myorder', views.myorder, name='myorder'),
    path('payment_success', views.payment_success, name='payment_success'),

]
