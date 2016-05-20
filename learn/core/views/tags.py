from tagging.views import TaggedObjectList
from cases.models import Article, Case


class TaggedArticleList(TaggedObjectList):
    template_name = "tags/article_tag_list.html"
    model = Article
    allow_empty = True


class TaggedCaseList(TaggedObjectList):
    template_name = "tags/case_tag_list.html"
    model = Case
    allow_empty = True
