from django.contrib import admin
from .models import Membre, Reunion, Cotisation, Projet, Financement, Versement

admin.site.register(Membre)
admin.site.register(Reunion)
admin.site.register(Cotisation)
admin.site.register(Projet)
admin.site.register(Financement)
admin.site.register(Versement)
