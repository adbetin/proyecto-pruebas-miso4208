from django.contrib import admin

# Register your models here.
from testcore.models import *

admin.site.register(ApplicationType)
admin.site.register(Application)
admin.site.register(TestType)
admin.site.register(Library)
admin.site.register(ApplicationTest)
admin.site.register(TestExecution)
