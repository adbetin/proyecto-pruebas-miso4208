from django.http import HttpResponse
from django.shortcuts import render
import os
import uuid

from tester.functions import create_file, delete_file, cypress_tester
from rest_framework.utils import json


# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def headless_cypress(request):
    return render(request, 'headless/cypress.html', {})


def headless_cypress_process(request):
    if request.method == 'POST':
        # get code
        code_content = request.POST[u'code_content']
        test_filename = "%s.%s" % (uuid.uuid4(), "spect.js")

        workspacefolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workspace", "headless", "\\test_hash000000")

        # crea el archivo
        # filename = create_file(workspacefolder, test_filename, code_content)

        cypress_tester("node_modules\\.bin\\cypress run", "D:\\uniandes Miso\\Pruebas Automaticas\\proyecto-pruebas-miso4208\\Proyecto\\workspace\\headless\\test_hash000000")

        # se elimina el archivo
        # delete_file(filename)

        return HttpResponse(
            json.dumps({"success": True, "response": "Ejecutado con exito", 'errors': []}),
            content_type="application/json", status=200)
    else:
        return HttpResponse(
            json.dumps({"success": False, "response": "Metodo no permitido", 'errors': ["Metodo no permitido"]}),
            content_type="application/json", status=500)


def headless_webdriver(request):
    return render(request, 'headless/webdriver.html', {})


def android(request):
    return render(request, 'random/android.html', {})


def calabash(request):
    return render(request, 'bdt/calabash.html', {})


def cucumber(request):
    return render(request, 'bdt/cucumber.html', {})
