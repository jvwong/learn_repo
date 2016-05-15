from django.test import TestCase
from datetime import date

from cases.models import Article, Case


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
            slug="a-slug"
        )

    def test_create(self):
        self.assertEqual(Article.objects.count(), 1)
        object = Article.objects.get(title="A title")
        self.assertEqual(object.title, "A title")
        self.assertEqual(object.authors, ['Author Last'])
        self.assertEqual(object.journal, 'A journal')
        self.assertIsInstance(object.pub_date, date)
        self.assertEqual(object.volume, 0)
        self.assertEqual(object.issue, 0)
        self.assertFalse(object.page_range.isempty)
        self.assertEqual(object.slug, 'a-slug')


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
            slug="a-slug"
        )

    def test_create(self):
        Case.objects.get_or_create(
            title="A title",
            subtitle="A subtitle",
            article=Article.objects.get(title="A title"),
            quick_summary={"1": "A summary"},
            author_profile="An author profile",
            context="A context",
            question="A  question",
            researcher_goals="A researcher goal",
            approach="An approach",
            summary="A summary",
            references={"1": "A reference"},
            quote="A quote",
            figure_legend="A figure legend",
            slug="a-slug"
        )

        self.assertEqual(Case.objects.count(), 1)