from django.contrib import admin
from .models import Article, Case
from sorl.thumbnail.admin import AdminImageMixin

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)


class CaseAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Case, CaseAdmin)
