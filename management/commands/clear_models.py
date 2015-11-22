from django.core.management.base import BaseCommand
from models import Gallery, Image


class Command(BaseCommand):

    def handle(self, *args, **options):
        Gallery.objects.all().delete()
        Image.objects.all().delete()
