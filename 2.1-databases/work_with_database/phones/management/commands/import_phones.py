import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('/home/chrnv/PycharmProjects/django/2.1-databases/work_with_database/phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone(name=phone['name'], image=phone['image'], price=phone['price'],
                              release_date=phone['release_date'], lte_exists=phone['lte_exists']).save()

