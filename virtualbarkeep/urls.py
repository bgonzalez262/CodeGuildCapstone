from django.urls import path
from . import views

app_name = 'virtualbarkeep'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.searchalc, name='searchalc')
]