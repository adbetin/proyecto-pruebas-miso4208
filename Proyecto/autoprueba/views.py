from django.shortcuts import render

# Create your views here.
import requests
def index(request):
    return render(request, 'index.html', {})

def android(request):
    return render(request, 'random/android.html', {})

def calabash(request):
    return render(request, 'bdt/calabash.html', {})

def cucumber(request):
    if(request.method == "POST"):
        print(request)
        print(request.POST.getlist('evento[]'))
        print(request.POST.getlist('type[]'))
        print(request.POST.getlist('finder[]'))


        url = 'http://192.168.100.156:8000/feature'
        data = '''{
    "feature_name": "'''+request.POST.get('featureName')+'''",
    "user_story": "'''+request.POST.get('userStory')+'''",
    "scenarios":
    [
        '''+getScenarios(request)+''',
        
        "then":
        {
            "type":"'''+request.POST.get('outputCond')+'''",
            "value":"'''+request.POST.get('exval')+'''"
        }	
        }
        ]
    }'''

        print(data)
        response = requests.post(url, data=data)
        return render(request, 'bdt/cucumber.html', {})
    else:
        return render(request, 'bdt/cucumber.html', {})

def getScenarios(req):
    data='''
    {
	"name": "'''+ req.POST.get('scenName')+'''",
	"given":"'''+req.POST.get('website')+'''",
	"steps":
	[
	'''+ getSteps(req)+'''
	]
    '''
    return data

def getSteps(req):
    data1=""

    for x in range(0, len(req.POST.getlist('evento[]'))):

        data1=data1+'''{
			"event": "'''+req.POST.getlist('evento[]')[x]+'''",
			"type": "'''+req.POST.getlist('type[]')[x]+'''",
			"finder":"'''+req.POST.getlist('finder[]')[x]+'''",
			"value":"'''+req.POST.getlist('value[]')[x]+'''"
		    }'''
        if x!=((len(req.POST.getlist('evento[]'))-1)):
            data1=data1+","
    return data1