from django.http import HttpResponse
from django.shortcuts import render
import os
import uuid
import threading

from tester.functions import create_file, mdroid_tester, cypress_tester
from rest_framework.utils import json

# Create your views here.
import requests


def index(request):
    return render(request, 'index.html', {})


def headless_cypress(request):
    return render(request, 'headless/cypress.html', {})


def headless_cypress_process(request):
    if request.method == 'POST':
        # get code
        code_content = request.POST[u'code_content']
        test_filename = "%s.%s" % (uuid.uuid4(), "spect.js")

        workspacefolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workspace", "headless",
                                       "\\test_hash000000")

        # crea el archivo
        # filename = create_file(workspacefolder, test_filename, code_content)

        cypress_tester()

        # se elimina el archivo
        # delete_file(filename)

        return HttpResponse(
            json.dumps({"success": True, "response": "Ejecutado con exito", 'errors': []}),
            content_type="application/json", status=200)
    else:
        return HttpResponse(
            json.dumps({"success": False, "response": "Metodo no permitido", 'errors': ["Metodo no permitido"]}),
            content_type="application/json", status=500)


def mutation_mdroid(request):
    return render(request, 'mutation/mdroid.html', {})


def mutation_mdroid_process(request):
    if request.method == 'POST':
        # get code
        options_generated = request.POST[u'code_content']
        multithread = request.POST[u'multithread']
        application = request.POST[u'application']

        mdroid_tester(application, options_generated, multithread, "/home/andresdavid/PruebasAutomaticas/S9")

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
    if (request.method == "POST"):
        print(request)
        print(request.POST.getlist('evento[]'))
        print(request.POST.getlist('type[]'))
        print(request.POST.getlist('finder[]'))

        url = 'http://192.168.100.156:8000/feature'
        data = '''{
    "feature_name": "''' + request.POST.get('featureName') + '''",
    "user_story": "''' + request.POST.get('userStory') + '''",
    "scenarios":
    [
        ''' + getScenarios(request) + ''',

        "then":
        {
            "type":"''' + request.POST.get('outputCond') + '''",
            "value":"''' + request.POST.get('exval') + '''"
        }
        }
        ]
    }'''

        print(data)
        response = requests.post(url, data=data)
        return render(request, 'bdt/cucumber.html', {})
    else:
        return render(request, 'bdt/cucumber.html', {})


def sqlGenerator(request):
    if (request.method == "POST"):
        print(request)
        print(request.POST.getlist('evento[]'))
        print(request.POST.getlist('type[]'))
        print(request.POST.getlist('finder[]'))

        url = 'http://192.168.64.2/generatedata-3.2.7/api/v1/data'
        data = '''{
    "numRows":''' + request.POST.get('numFilas') + ''',
    "rows": [
       ''' + getRows(request) + '''
    ],
    "export": {
        "type": "SQL",
        "settings": {
        	"tableName":"''' + request.POST.get('tableName') + '''",
        	"databaseType":"''' + request.POST.get('motor') + '''",
            "stripWhitespace": false,
            "dataStructureFormat": "simple"
        }
    }
}'''

        response = requests.post(url, data=data)

        return HttpResponse(response.content, content_type='text/plain')
    else:
        return render(request, 'sqlGenerator/sqlGenerator.html', {})


def getScenarios(req):
    data = '''
    {
	"name": "''' + req.POST.get('scenName') + '''",
	"given":"''' + req.POST.get('website') + '''",
    "steps":
    [
	''' + getSteps(req) + '''
    ]
    '''
    return data


def getSteps(req):
    data1 = ""

    for x in range(0, len(req.POST.getlist('evento[]'))):

        data1 = data1 + '''{
			"event": "''' + req.POST.getlist('evento[]')[x] + '''",
			"type": "''' + req.POST.getlist('type[]')[x] + '''",
			"finder":"''' + req.POST.getlist('finder[]')[x] + '''",
			"value":"''' + req.POST.getlist('value[]')[x] + '''"
            }'''
        if x != (len(req.POST.getlist('evento[]')) - 1):
            data1 = data1 + ","
    return data1


def getRows(req):
    data1 = ""
    for x in range(0, len(req.POST.getlist('nombreColumna[]'))):
        print(x)
        if (req.POST.getlist('column[]')[x] == 'Alfanumérico'):
            data1 = data1 + ''' {
                 "type": "AlphaNumeric",
                "title": "''' + req.POST.getlist('nombreColumna[]')[x] + '''",
                 "settings": {
                "placeholder": "LLLxxLLLxLL"
                 }
                 }'''
        elif (req.POST.getlist('column[]')[x] == 'Autoincremento'):
            data1 = data1 + '''{
                    "type": "AutoIncrement",
                    "title": "''' + req.POST.getlist('nombreColumna[]')[x] + '''",
                     "settings": {
                     "incrementStart": 1,
                     "incrementValue": 1
                    }}'''
        elif (req.POST.getlist('column[]')[x] == 'Booleano'):
            data1 = data1 + '''{
                 "type": "Boolean",
                 "title": "''' + req.POST.getlist('nombreColumna[]')[x] + '''",
                 "settings": {  "placeholder": "False|True"  } 
                }'''

        if x != ((len(req.POST.getlist('column[]')) - 1)):
            data1 = data1 + ","
    return data1


def vrtcypress(request):
    return render(request, 'vrt/cypress.html', {})

def vrtresemble(request):
    return render(request, 'vrt/resemble.html', {})


def configListado(request):
    return render(request, 'config/configListado.html', {})

def configPlataforma(request):
    return render(request, 'config/configPlataforma.html', {})

def appMoviles(request):
    return render(request, 'config/listadoAppWeb.html', {})

def appWeb(request):
    return render(request, 'config/listadoAppMovil.html', {})
