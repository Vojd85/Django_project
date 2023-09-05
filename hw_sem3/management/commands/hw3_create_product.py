from django.core.management.base import BaseCommand, CommandParser
from hw_sem3.models import Product

class Command(BaseCommand):
    help = "Create new product"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('count', type=int, help='Product count')
        parser.add_argument('-d', type=str, nargs='*', help='Product description')

    def handle(self, *args, **options) -> str | None:
        product = Product(name=options['name'], price=options['price'], count=options['count'], description=' '.join(options['d']))
        product.save()

    # description = models.TextField()
    # date_income = models.DateField(auto_now=True)