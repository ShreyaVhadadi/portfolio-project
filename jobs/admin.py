from django.contrib import admin

from .models import Job
from .models import Contact

admin.site.register(Job)

admin.site.register(Contact)