from django.views.generic import ListView, DetailView
from .models import Case


class CaseList(ListView):
    template_name = "cases/case_list.html"
    model = Case


class CaseDetail(DetailView):
    template_name = "cases/case_detail.html"
    model = Case
