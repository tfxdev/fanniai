from django.contrib import admin
from .models import *

admin.site.register(Candidate)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Package)
admin.site.register(PackageFeature)
