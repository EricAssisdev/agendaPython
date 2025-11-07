from django.contrib import admin
from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'categoria', 'favorito', 'criado_em']
    list_filter = ['categoria', 'favorito', 'criado_em']
    search_fields = ['nome', 'email', 'telefone', 'celular', 'empresa']
    list_editable = ['favorito']
    date_hierarchy = 'criado_em'
    ordering = ['nome']
