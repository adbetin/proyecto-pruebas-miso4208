from django.shortcuts import render
import os
import subprocess
from django.http import HttpResponse

# Create your views here.

def android(request , numEvent, packageHerramienta):
    os.chdir('/home/rafa/Android/Sdk/platform-tools/')
    os.system("./adb shell monkey -p  "+ packageHerramienta +" -v "+ numEvent)

    return HttpResponse( True )