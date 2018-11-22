from django.contrib import admin

# Register your models here.
from testcore.models import *

admin.site.register(ApplicationType)
admin.site.register(Application)
admin.site.register(TestType)
admin.site.register(Library)
admin.site.register(ApplicationTest)
#admin.site.register(TestExecution)

class TestExecutionAdmin(admin.ModelAdmin):
    list_display = ('applicationTest', 'status')
    list_filter = ('applicationTest', 'status')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'


admin.site.register(TestExecution, TestExecutionAdmin)