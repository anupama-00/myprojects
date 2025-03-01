from django.contrib import admin

from employee.models import Jobapply

from employee.models import SavedJob

# Register your models here.
admin.site.register(Jobapply)
admin.site.register(SavedJob)