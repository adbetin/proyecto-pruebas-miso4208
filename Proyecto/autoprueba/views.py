from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def android(request):
    return render(request, 'random/android.html', {})

def calabash(request):
    return render(request, 'bdt/calabash.html', {})

def cucumber(request):
    return render(request, 'bdt/cucumber.html', {})