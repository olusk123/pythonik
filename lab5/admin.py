from django.contrib import admin
from .models import Person, Team, Osoba

admin.site.register(Person)
admin.site.register(Team)

class OsobaAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'data_dodania')
    search_fields = ('nazwa',)

admin.site.register(Osoba, OsobaAdmin)