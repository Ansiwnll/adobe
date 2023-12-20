from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    # path('', views.clothes, name='clothes'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
]
