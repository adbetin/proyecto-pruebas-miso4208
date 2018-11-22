from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
import json
import os
def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def create_feature(request):
    if request.method == 'POST':
        info = json.loads(request.body)
        feature_name = info['feature_name']
        user_story = info['user_story']
        scenarios=info['scenarios']
        try:
            create_File(info);
            os.system('./executeTest.sh')
            response = json.dumps([{ 'Success': scenarios[0]}])
        except:
            response = json.dumps([{ 'Error': 'Car could not be added!'}])
    return HttpResponse(response, content_type='text/json')

def create_File(info):
    file = open (os.path.expanduser("~//Documents//Universidad//Pruebas automaticas//proyecto//Cucumber//cucumber-webdriverio//features//"+info['feature_name']+".feature"),"w")
    file.write("Feature: "+info['feature_name']+"\n")
    file.write("\t"+info['user_story']+"\n")
    for scenario in info['scenarios']:
        file.write(create_Scenario(scenario))
    file.close()

def create_Scenario(scenario):
    sce="Scenario: "+scenario['name']+"\n";
    sce=sce+"\t Given I go to "+scenario['given']+"\n"
    flag=0
    for step in scenario['steps']:
        sce=sce+"\t"+create_Step(step,flag)+"\n"
        flag=flag+1
    sce=sce+"\t Then I expect to see "+scenario['then']['value']+" "+scenario['then']['type']
    print(sce)
    return sce

def create_Step(step,flag):
    st=""
    if(flag==0):
        st="When "+get_StepContent(step)
    else:
        st="And "+get_StepContent(step)
    return st

def get_StepContent(step):
    st=""
    if(step['event']=="click"):
        st="I click "
        if(step['type']=="button"):
            st=st+step['finder']+" button"
        elif(step['type']=="input"):
            st=st+step['finder']+" input"
        elif(step['type']=="link"):
            st=st+step['finder']+" link text"
    elif(step['event']=="wait"):
        st="I wait "+step['value']+" milliseconds"
    elif(step['event']=="fill input"):
        st="I fill "+step['finder']+" input with "+step['value']
        print(st)
    elif(step['event']=="press"):
        st="I press "+step['value']+" key"
    return st
