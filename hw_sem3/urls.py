from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/<int:client_id>/<str:time>/', views.get_products, name='all_products'),
]