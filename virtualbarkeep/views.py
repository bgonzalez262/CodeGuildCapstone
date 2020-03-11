from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'virtualbarkeep/index.html')

def search_alc(request):
    return render(request,'virtualbarkeep/searchdrink.html')

