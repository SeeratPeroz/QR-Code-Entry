from django.contrib import admin
from entry.models import *


# Register your models here to show it in admin panel.
admin.site.register(Patient)
admin.site.register(Entry)
admin.site.register(Employee)
