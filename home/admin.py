# Register your models here.
from django.contrib import admin
from .models import Personagem

class PersonagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Idade', 'Espécie', 'Ocupação', )
    list_display_links = ('Nome',)
    search_fields = ('Nome', )

admin.site.register(Personagem, PersonagemAdmin)

