from django.db import models
from django.contrib.auth.models import User



class Event(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' ' + self.name

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class SavedDrink(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    instruction = models.CharField(max_length=400)
    ingredient = models.CharField(max_length=300)
    measurement = models.CharField(max_length=300)
    image = models.CharField(max_length=300)


    def __str__(self):
        return self.user.username + ' ' + self.name

class SavedFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    api_id = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username + ' ' + self.name

class EventItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    drinks = models.ForeignKey(SavedDrink, on_delete=models.PROTECT)
    food = models.ForeignKey(SavedFood, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username + ':' + self.event.name

