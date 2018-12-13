import os

from django.http import HttpResponse

# Create your views here.
from testcore.models import Application
from tester.tasks import random_testing


def android(request, numEvent, applicationId):
    app = Application.objects.get(id=applicationId)
    random_testing.delay(applicationId, numEvent, app.package_name)

    # os.chdir('/home/rafa/Android/Sdk/platform-tools/')
    # os.system("./adb shell monkey -p  " + app.package_name + " -v " + numEvent)

    return HttpResponse(True)
