from django.db import models
from django.contrib.auth.models import User



class Event(models.Model):
    name = models.CharField(max_length=200)
    attendees = models.IntegerField(default=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' ' + self.name


class SavedDrink(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='drinks', null=True, blank=True)
    add_fav = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    instruction = models.CharField(max_length=400)
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username + ' ' + self.name

class SavedDrinkIngredient(models.Model):
    drink = models.ForeignKey(SavedDrink, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return self.drink.name + ' ' + self.name

class SavedFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    api_id = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username + ' ' + self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DrinkList(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    drink_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ':' + self.drink_id





