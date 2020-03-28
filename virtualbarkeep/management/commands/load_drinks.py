from django.core.management.base import BaseCommand
import json
from virtualbarkeep.models import DrinkList


class Command(BaseCommand):
    def handle(self,*args,**options):
        with open(r'C:\Users\Brandon\code\Capstone\CodeGuildCapstone\virtualbarkeep\management\commands\drink_list.json', 'r') as f:
            data = json.loads(f.read())
        for drink in data['drinks']:
            name = drink['name']
            image = drink['image']
            id = drink['drinkId']
            uploaded = DrinkList(name=name, image=image, drink_id=id)
            uploaded.save()