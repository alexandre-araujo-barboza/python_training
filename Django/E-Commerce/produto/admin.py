from django.contrib import admin
from .models import Produto, Variacao

class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'descricao_curta',
        'format_price_marketing',
        'format_price_marketing_promotional',
    ]
    inlines = [
        VariacaoInLine, 
    ]
    
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
