from django.urls import path
from . import views

app_name = 'vbk'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.searchalc, name='searchalc'),
    path('searchfood/', views.searchfood, name='searchfood'),
    path('register/', views.register, name='register' ),
    path('login_user/', views.login_user, name='login_user'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('savete/', views.ste, name='ste'),
    path('savetf/', views.stf, name='stf'),
    path('create/', views.add_event, name='add_event'),
    path('events/<int:event_id>/', views.event_view, name='event_view'),


]