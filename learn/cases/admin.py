from django.contrib import admin
from .models import Article, Case


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)


class CaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Case, CaseAdmin)
