from django.contrib import admin
from .models import  Poziadavka_ee
from .models import  User

# Register your models Poziadavky EE.

class StlpcePoziadaviek(admin.ModelAdmin):
	list_display = ('kod_spravy','eic','datum_vytvorenia','datum_zaciatku_zmluvy_zmeny')

admin.site.register(Poziadavka_ee,StlpcePoziadaviek)