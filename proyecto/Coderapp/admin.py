from django.contrib import admin

from . import models

admin.site.register(models.Coordinador)
admin.site.register(models.Empleado)
admin.site.register(models.Area)