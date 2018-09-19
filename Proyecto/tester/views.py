from django.shortcuts import render
import os

# Create your views here.

def android(request):
    os.listdir('.')
    os.system("start /wait cmd ")