from django.contrib import admin

# Register your models here.
from .models import House_refer, Refer
admin.site.register(House_refer)
admin.site.register(Refer)
