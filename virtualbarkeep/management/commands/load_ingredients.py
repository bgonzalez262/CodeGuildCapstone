from django.core.management.base import BaseCommand
import json
from virtualbarkeep.models import Ingredient


class Command(BaseCommand):
    def handle(self,*args,**options):
        with open(r'C:\Users\Brandon\code\Capstone\CodeGuildCapstone\virtualbarkeep\management\commands\ingredients.json', 'r') as f:
            data = json.loads(f.read())
        for ingredient in data['ingredients']:
            ingredient = ingredient['name']
            ingredient = Ingredient(name=ingredient)
            ingredient.save()