import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as f:
            phones = csv.reader(f, delimiter=';')
            next(phones)
            for i in phones:
                phone = Phone(id=i[0],
                              name=i[1],
                              image=i[2],
                              price=i[3],
                              release_date=i[4],
                              lte_exists=i[5],
                              slug=slugify(i[1])
                )
                print(phone)
                phone.save()
