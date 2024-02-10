from django.shortcuts import render, redirect
from pygame.locals import *
import pygame
from django.contrib.auth.views import LoginView
# Create your views here.
def home(request):
    return render(request,'home.html')
def mächtigeTricks(request):
    return render(request, 'tricks.html')