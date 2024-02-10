from django.urls import path
from .views import *
urlpatterns = [
   path('', home, name='home'),
   path('home/', home, name='home'),
   path('home/mächtige-tricks/', mächtigeTricks, name='machtige-tricks'),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),
  #path('', , name=''),

]