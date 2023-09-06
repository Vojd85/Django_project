from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_product/', views.add_product, name='add_product'),
    path('change_product/<int:product_id>/', views.change_product, name='change_product'),

]