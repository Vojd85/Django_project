from django.shortcuts import render
from .models import Order, Product, Client
from datetime import date, timedelta


def index(request):
    products = Product.objects.all()
    return render(request, 'hw_sem3/index.html', {'products': products})

def get_products(request, client_id, time):
    time_choice = {'week': timedelta(days=7), 'month': timedelta(days=30), 'year': timedelta(days=365)}.get(time)
    orders = Order.objects.filter(client__pk=client_id, order_date__gte=date.today() - time_choice)
    client = Client.objects.filter(pk=client_id).first()
    products = set()
    for order in orders:
        for product in order.products.all():
            products.add(product)
    return render(request, 'hw_sem3/products.html', {'products': products, 'time': time, 'client': client})