from django.contrib import admin
from .models import VagaEmprego

# Register your models here.
@admin.register(VagaEmprego)
class VagaEmpregoAdmin(admin.ModelAdmin):
    list_display = ('id', 'telefone_contato', 'data_cadastro', 'ativo')
    list_filter = ('ativo', 'data_cadastro')
    search_fields = ('descricao', 'telefone_contato')
    date_hierarchy = 'data_cadastro'