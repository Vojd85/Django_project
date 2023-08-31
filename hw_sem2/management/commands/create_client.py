from django.core.management.base import BaseCommand, CommandParser
from hw_sem2.models import Client

class Command(BaseCommand):
    help = "Create new client"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client Email')
        parser.add_argument('phone', type=int, help='Client phone, only digits')
        parser.add_argument('-a', type=str, nargs='*', help='Client adress')

    def handle(self, *args, **options) -> str | None:
        client = Client(name=options['name'], email=options['email'], phone=options['phone'], adress=' '.join(options['a']))
        client.save()

