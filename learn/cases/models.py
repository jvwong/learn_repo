from django.db import models
from core.models import TimeStampedModel
from django.contrib.postgres.fields import ArrayField, IntegerRangeField, JSONField
from django.core.urlresolvers import reverse
from markupfield.fields import MarkupField
from tagging.fields import TagField


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

    url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=250)
    tags = TagField(help_text="Separate tags with commas.")

    class Meta:
        ordering = ["pub_date"]
        verbose_name_plural = "articles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.slug)])


def case_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/instance.slug/<filename>
    return 'case/{0}/{1}'.format(instance.slug, filename)


class Case(TimeStampedModel):
    title = models.CharField(max_length=250, unique=True)
    subtitle = models.CharField(max_length=250, blank=True)
    article = models.OneToOneField(Article)
    quick_summary = MarkupField(blank=True,
                                markup_type='markdown',
                                help_text='Markdown enabled')
    author_profile = MarkupField(blank=True,
                                 markup_type='markdown',
                                 help_text='Markdown enabled')
    context = MarkupField(blank=True,
                          markup_type='markdown',
                          help_text='Markdown enabled')
    question = MarkupField(blank=True,
                           markup_type='markdown',
                           help_text='Markdown enabled')
    researcher_goals = MarkupField(blank=True,
                                   markup_type='markdown',
                                   help_text='Markdown enabled')
    approach = MarkupField(blank=True,
                           markup_type='markdown',
                           help_text='Markdown enabled')
    summary = MarkupField(blank=True,
                          markup_type='markdown',
                          help_text='Markdown enabled')
    references = MarkupField(blank=True,
                             markup_type='markdown',
                             help_text='Markdown enabled')
    quote = MarkupField(blank=True,
                        markup_type='markdown',
                        help_text='Markdown enabled')

    figure = models.ImageField(upload_to=case_directory_path, blank=True)
    figure_legend = MarkupField(blank=True,
                                markup_type='markdown',
                                help_text='Markdown enabled')
    pdf = models.FileField(upload_to=case_directory_path, blank=True)

    slug = models.SlugField(unique=True, max_length=250)
    tags = TagField(help_text="Separate tags with commas.")

    class Meta:
        ordering = ["created"]
        verbose_name_plural = "cases"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('case-detail', args=[str(self.slug)])

# # Receive the pre_delete signal and delete the file associated with the model instance.
# from django.db.models.signals import pre_delete
# from django.dispatch.dispatcher import receiver
#
# @receiver(pre_delete, sender=Case)
# def mymodel_delete(sender, instance, **kwargs):
#     # Pass false so FileField doesn't save the model.
#     if hasattr(instance, 'figure'):
#         if hasattr(instance.figure, 'name'):
#             print(instance.figure.name)
#             # instance.figure.delete(False)
#
#     # if hasattr(instance, 'pdf'):
#         # instance.pdf.delete(False)
