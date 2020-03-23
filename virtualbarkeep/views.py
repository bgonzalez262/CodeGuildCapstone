from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import SavedDrink, SavedFood, Event, SavedDrinkIngredient
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
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
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
    image = data['image']
    addfav = False
    saveddrink = SavedDrink(add_fav=addfav, name=drink, image=image, instruction=instruction, user=request.user,event=event)
    saveddrink.save()
    for ingredient in data['ingredients']:
        savedingredient = SavedDrinkIngredient(drink=saveddrink, name=ingredient['name'], amount=ingredient['amount'])
        savedingredient.save()
    print(data)
    return HttpResponseRedirect(reverse('vbk:profile'))

def modalSte(request,drink_id):
    drink = SavedDrink.objects.get(id=drink_id)
    event_id = request.POST['event_id']
    drink.event_id = event_id
    drink.save()
    print(drink)
    return HttpResponseRedirect(reverse('vbk:profile'))


# save drink to favorites. Shown on the profile page.
@login_required
def stf(request):

    data = json.loads(request.body)

    print(data)
    drink = data['name']
    instruction = data['instructions']
    image = data['image']
    addfav = True
    saveddrink = SavedDrink(add_fav=addfav, name=drink, image=image, instruction=instruction, user=request.user)
    saveddrink.save()
    for ingredient in data['ingredients']:
        savedingredient = SavedDrinkIngredient(drink=saveddrink, name=ingredient['name'], amount=ingredient['amount'])
        savedingredient.save()
    print(data)
    return HttpResponseRedirect(reverse('vbk:profile'))

# Log in required. Displays selectable event for viewing and favorite drinks---
@login_required
def profile(request):
    events = Event.objects.all().filter(user=request.user)
    drinks = SavedDrink.objects.all().filter(user=request.user, add_fav=True)
    ingredients = SavedDrinkIngredient.objects.all()
    has_favorites = request.user.saveddrink_set.filter(add_fav=True).count()>0
    context = {
        'events': events,
        'drinks': drinks,
        'ingredients': ingredients,
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
    return render(request, 'virtualbarkeep/events.html', context)

def event_data(request, event_id):
    event = Event.objects.get(id=event_id)
    data = {
        'event_name': event.name,
        'attendees': event.attendees,
        'drinks': [],
    }

    for drink in event.drinks.all():
        ingredients = []
        for ingredient in drink.ingredients.all():
            ingredients.append({
                'name':ingredient.name,
                'amount':ingredient.amount,
            })
            print(ingredient.name)

        data['drinks'].append({
            'name': drink.name,
            'instructions': drink.instruction,
            'image': drink.image,
            'ingredients': ingredients,
            })
    return JsonResponse(data)




