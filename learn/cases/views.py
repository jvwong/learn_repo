from django.views.generic import ListView, DetailView
from .models import Case, Article


class ArticleList(ListView):
    template_name = "cases/article_list.html"
    model = Article


class ArticleDetail(DetailView):
    template_name = "cases/article_detail.html"
    queryset = Article.objects.all()


class CaseList(ListView):
    template_name = "cases/case_list.html"
    model = Case


class CaseDetail(DetailView):
    template_name = "cases/case_detail.html"
    queryset = Case.objects.select_related('article')
