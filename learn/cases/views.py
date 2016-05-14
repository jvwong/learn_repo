from django.views.generic import ListView
from .models import Article


class CaseList(ListView):
    template_name = "cases/case_list.html"
    model = Article
