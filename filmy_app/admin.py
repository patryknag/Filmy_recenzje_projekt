from django.contrib import admin
from .models import Gatunek, Film, Recenzent, Opinia, Ocena

# Register your models here.
admin.site.register(Gatunek)
admin.site.register(Film)
admin.site.register(Recenzent)
admin.site.register(Opinia)
admin.site.register(Ocena)
