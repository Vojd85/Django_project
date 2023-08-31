from django.core.management.base import BaseCommand
from hw_sem2.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Create new order'

    def add_arguments(self, parser):
        parser.add_argument('client', type=int, help='Client ID')
        parser.add_argument('products_id', nargs='*', type=int, help='Enter products id with split')

    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk=kwargs['client']).first()
        if client and kwargs['products_id']:
            order_price = 0
            products_list = []
            for id in kwargs['products_id']:
                product = Product.objects.filter(pk=id).first()
                if product:
                    order_price += product.price
                    products_list.append(product)
            order = Order(client=client, order_price=order_price)
            order.save()
            order.products.set(products_list)

    