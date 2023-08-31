from django.core.management.base import BaseCommand, CommandParser
from hw_sem2.models import Client

class Command(BaseCommand):
    help = "Delete client by ID"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int, help='Client ID need to delete')

    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk=kwargs['id']).first()
        if client:
            client.delete()