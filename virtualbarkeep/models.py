from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username + ' ' + self.name

class SavedDrink(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    api_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username + ' ' + self.name

class SavedFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    api_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username + ' ' + self.name

