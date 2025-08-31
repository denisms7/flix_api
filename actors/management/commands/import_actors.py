import csv
from django.core.management.base import BaseCommand
from datetime import datetime
from actors.models import Actor
from django.db import IntegrityError, DataError

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Caminho do Arquivo CSV com atores.'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']
                
                try:
                    Actor.objects.create(
                        name=name,
                        birthday=birthday,
                        nationality=nationality,
                    )
                    print(f'🆗 Importado: {name}')
                except (IntegrityError, DataError) as e:
                    print(f'⛔ Não Importado: {name} -> {e}')
                except Exception as e:
                    print(f'⚠️ Erro inesperado ao importar {name}: {e}')
