from django.contrib import admin
from liste.models import Prestation, Devis

class PrestationAdmin(admin.ModelAdmin):
    list_display = ('artiste', 'titre_spectacle')

class DevisAdmin(admin.ModelAdmin):
    list_display = ('numero', 'objet')

admin.site.register(Prestation, PrestationAdmin)
admin.site.register(Devis, DevisAdmin)
