from django.db import models
from core.models import TimeStampedModel


class Journal(TimeStampedModel):
    name = models.CharField(unique=True, max_length=250)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "journals"

    def __str__(self):
        return self.name


class Author(TimeStampedModel):
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=2, blank=True)
    last_name = models.CharField(max_length=50)

    class Meta:
        ordering = ["last_name"]
        unique_together = ("first_name", "last_name")
        verbose_name_plural = "authors"

    def __str__(self):
        return "{0}, {1}".format(self.last_name, self.first_name)


class Article(TimeStampedModel):
    title = models.CharField(max_length=250)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True)
    volume = models.IntegerField(null=True)
    issue = models.IntegerField(null=True, blank=True)
    start_page = models.IntegerField(null=True)
    end_page = models.IntegerField(null=True, blank=True)
    authors = models.ManyToManyField('Author')
    slug = models.SlugField(unique=True, max_length=250)
    pub_date = models.DateField(null=True)

    class Meta:
        ordering = ["pub_date"]
        verbose_name_plural = "articles"

    def __str__(self):
        return self.title
