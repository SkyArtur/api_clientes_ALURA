from django.contrib import admin
from clientes.models import Cliente


# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'ativo')
    list_display_links = ('id', 'nome')
    list_editable = ('ativo',)
    list_per_page = 10
    search_fields = ('nome', 'cpf', 'rg')
    ordering = ('nome',)
