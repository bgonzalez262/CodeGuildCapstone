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
    path('modalSte/<int:drink_id>/', views.modalSte, name='modalSte'),
    path('savetf/', views.stf, name='stf'),
    path('create/', views.add_event, name='add_event'),
    path('events/<int:event_id>/', views.event_view, name='event_view'),
    path('event_data/<int:event_id>/', views.event_data, name='event_data'),
    path('listdrinks/', views.search_list_drinks, name='listdrinks'),
    path('delete/<int:drink_id>/', views.delete_drink, name="delete"),


]