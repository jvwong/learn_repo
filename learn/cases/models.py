from django.db import models
from core.models import TimeStampedModel
from django.contrib.postgres.fields import ArrayField, IntegerRangeField
from django.core.urlresolvers import reverse

class Article(TimeStampedModel):
    title = models.CharField(max_length=250)
    authors = ArrayField(
        models.CharField(max_length=100, blank=True),
        size=200
    )
    journal = models.CharField(max_length=250)
    pub_date = models.DateField()
    volume = models.IntegerField()
    issue = models.IntegerField(blank=True, null=True)
    page_range = IntegerRangeField()

    slug = models.SlugField(unique=True, max_length=250)

    class Meta:
        ordering = ["pub_date"]
        verbose_name_plural = "articles"

    def __str__(self):
        return self.title


class Case(TimeStampedModel):
    title = models.CharField(max_length=250, unique=True)
    subtitle = models.CharField(max_length=250, blank=True)
    article = models.OneToOneField(Article)
    summary = ArrayField(
        models.CharField(max_length=250, blank=True),
        size=10,
        blank=True
    )
    author_profile = models.TextField(blank=True)
    context = models.TextField(blank=True)
    question = models.TextField(blank=True)
    researcher_goals = models.TextField(blank=True)
    approach = models.TextField(blank=True)
    references = ArrayField(
        models.CharField(max_length=500, blank=True),
        size=20,
        blank=True
    )
    quote = models.TextField(blank=True)
    figure = models.ImageField(upload_to='images/', blank=True)
    figure_legend = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=250)

    class Meta:
        ordering = ["created"]
        verbose_name_plural = "cases"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('case-detail', args=[str(self.slug)])
