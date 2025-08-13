from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'data_criacao')
    search_fields = ('nome',)
    list_filter = ('data_criacao',)
    # prepopulated_fields = {'slug': ('nome',)}  # caso tenha campo slug
