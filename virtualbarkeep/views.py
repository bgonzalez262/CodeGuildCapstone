from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'virtualbarkeep/index.html')

def searchalc(request):
    return render(request,'virtualbarkeep/search.html')

