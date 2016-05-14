from django.contrib import admin
from .models import Author, Article, Journal

class JournalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Journal, JournalAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
