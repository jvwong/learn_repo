from django.test import TestCase
from datetime import date

from cases.models import Article, Case

# Running:

class ArticleTests(TestCase):
    def setUp(self):
        Article.objects.get_or_create(
            title="A title",
            authors=['Author Last'],
            journal="A journal",
            pub_date=date.today(),
            volume=0,
            issue=0,
            page_range=(0, 1),
            url="http://www.example.com",
            slug="a-slug",
            tags="one, two, three"
        )

    def test_create(self):
        self.assertEqual(Article.objects.count(), 1)
        obj = Article.objects.get(title="A title")
        self.assertEqual(obj.title, "A title")
        self.assertEqual(obj.authors, ['Author Last'])
        self.assertEqual(obj.journal, 'A journal')
        self.assertIsInstance(obj.pub_date, date)
        self.assertEqual(obj.volume, 0)
        self.assertEqual(obj.issue, 0)
        self.assertEqual(obj.url, "http://www.example.com")
        self.assertFalse(obj.page_range.isempty)
        self.assertEqual(obj.slug, 'a-slug')


class CaseTests(TestCase):
    def setUp(self):
        Article.objects.get_or_create(
            title="A title",
            authors=['Author Last'],
            journal="A journal",
            pub_date=date.today(),
            volume=0,
            issue=0,
            page_range=(0, 1),
            url="http://www.example.com",
            slug="a-slug"
        )

    def test_create(self):
        Case.objects.get_or_create(
            title="A title",
            subtitle="A subtitle",
            article=Article.objects.get(title="A title"),
            quick_summary="A summary",
            author_profile="An author profile",
            context="A context",
            question="A  question",
            researcher_goals="A researcher goal",
            approach="An approach",
            summary="A summary",
            references="A reference",
            quote="A quote",
            figure_legend="A figure legend",
            slug="a-slug",
            tags="one, two, three"
        )

        self.assertEqual(Case.objects.count(), 1)