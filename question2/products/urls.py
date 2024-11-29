from django.urls import path
from . import views

urlpatterns = [
    path('products', views.create_product, name='create_product'),
    path('products', views.list_products, name='list_products'),
]
