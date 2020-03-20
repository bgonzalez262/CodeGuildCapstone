from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import SavedDrink, SavedFood, Event
from django.contrib.auth.decorators import login_required
import json


# Create your views here.
def index(request):
    return render(request, 'virtualbarkeep/index.html')


def searchalc(request):
    events = Event.objects.all().filter(user=request.user)
    context = {
        'events':events,

    }
    return render(request, 'virtualbarkeep/search.html', context)

def searchfood(request):
    return render(request, 'virtualbarkeep/food.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'virtualbarkeep/login.html')
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    User.objects.create_user(username, email, password)

    return HttpResponseRedirect(reverse('vbk:index'))


def add_event(request):
    event_name = request.POST['eventname']
    attendees = request.POST['attendees']
    user = request.user
    saveevent = Event(name=event_name, attendees=attendees, user=user)
    saveevent.save()
    return HttpResponseRedirect(reverse('vbk:profile'))


def login_page(request):
    return render(request, 'virtualbarkeep/login.html')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'virtualbarkeep/login.html')
    username = request.POST['username']
    password = request.POST['password']
    next = request.GET.get('next', '')
    print(request.POST)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if next != '':
            return HttpResponseRedirect(next)
        return HttpResponseRedirect(reverse('vbk:index'))
    if next == '':
        return HttpResponseRedirect(reverse('vbk:login') + '?message=failure')
    return HttpResponseRedirect(reverse('vbk:profile') + '?message=failure&next=' + next)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('vbk:index'))


# login required for the following views---

# save selected drink to event. User is given choices for which event to save to.
@login_required
def ste(request):
    data = json.loads(request.body)
    drink = data['name']
    event_id = data['event']
    event = Event.objects.get(id=event_id)
    print(event)
    instruction = data['instructions']
    ingredients_save = ''
    measurements_save = ''
    for i in range(len(data['ingredients'])):
        ingredient_name = data['ingredients'][i]['name']
        ingredients_save += ingredient_name + ','
    for i in range(len(data['ingredients'])):
        measurement = data['ingredients'][i]['amount']
        measurements_save += measurement + ','
    image = data['image']
    addfav = False
    saveddrink = SavedDrink(add_fav=addfav, name=drink, image=image, instruction=instruction, ingredient=ingredients_save, measurement=measurements_save, user=request.user,event=event)
    saveddrink.save()
    print(data)
    return HttpResponseRedirect(reverse('vbk:profile'))


# save drink to favorites. Shown on the profile page.
@login_required
def stf(request):
    data = json.loads(request.body)
    drink = data['name']
    instruction = data['instructions']
    ingredients_save = ''
    measurements_save = ''
    for i in range(len(data['ingredients'])):
        ingredient_name = data['ingredients'][i]['name']
        ingredients_save += ingredient_name + ','
    for i in range(len(data['ingredients'])):
        measurement = data['ingredients'][i]['amount']
        measurements_save += measurement + ','
    image = data['image']
    addfav = True
    saveddrink = SavedDrink(add_fav=addfav, name=drink, image=image, instruction=instruction,
                            ingredient=ingredients_save, measurement=measurements_save, user=request.user)
    saveddrink.save()
    print(data)
    alert("Saved!")
    return HttpResponseRedirect(reverse('vbk:profile'))

# Log in required. Displays selectable event for viewing and favorite drinks---
@login_required
def profile(request):
    events = Event.objects.all().filter(user=request.user)
    drinks = SavedDrink.objects.all().filter(user=request.user, add_fav=True)
    has_favorites = request.user.saveddrink_set.filter(add_fav=True).count()>0
    context = {
        'events': events,
        'drinks': drinks,
        'has_favorites': has_favorites,
    }
    return render(request, 'virtualbarkeep/profile.html', context)

# Single event view pages with all even data, including drinks and attendees.
@login_required
def event_view(request,event_id):
    event = Event.objects.get(id=event_id)
    
    context = {
        'event': event,
    }
    print(event.drink)
    return render(request, 'virtualbarkeep/events.html', context)

