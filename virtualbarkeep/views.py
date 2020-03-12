from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'virtualbarkeep/index.html')

def searchalc(request):
    return render(request,'virtualbarkeep/search.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'virtualbarkeep/reglog.html')
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    User.objects.create_user(username, email, password)

    return HttpResponseRedirect(reverse('vbk:index'))

def login_page(request):
    return render(request,'virtualbarkeep/login.html')

def login_user(request):
    if request.method == 'GET':
        return render(request, 'virtualbarkeep/login.html')
    username = request.POST['username']
    password = request.POST['password']
    next = request.GET.get('next','')
    print(request.POST)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        if next != '':
            return HttpResponseRedirect(next)
        return HttpResponseRedirect(reverse('vbk:index'))
    if next == '':
        return HttpResponseRedirect(reverse('vbk:login') + '?message=failure')
    return HttpResponseRedirect(reverse('vbk:profile') + '?message=failure&next='+next)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('vbk:index'))

@login_required
def profile(request):
    return render(request, 'vbk/reglog.html')

'''TODO
-finish adding the users and test register page
-set up "add to" feature, view and profile page
-model creation
'''