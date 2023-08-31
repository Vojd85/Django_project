from django.core.management.base import BaseCommand, CommandParser
from hw_sem2.models import Client

class Command(BaseCommand):
    help = "Update client by ID"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int, help='Client ID need to update')
        parser.add_argument('-n', type=str, help='Client name')
        parser.add_argument('-e', type=str, help='Client Email')
        parser.add_argument('-p', type=int, help='Client phone, only digits')
        parser.add_argument('-a', type=str, nargs='*', help='Client adress')

    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk=kwargs['id']).first()
        if client:
            if kwargs['n']:
                client.name = kwargs['n']
            if kwargs['e']:
                client.email = kwargs['e']
            if kwargs['p']:
                client.phone = kwargs['p']
            if kwargs['a']:
                client.adress = ' '.join(kwargs['a'])
            client.save()
            
