from django.test import TestCase
from django.core.urlresolvers import reverse


class ArticleTests(TestCase):
    def setUp(self):
        self.path = "/articles/"
        self.slug = "some-slug"

    def test_list(self):
        url = reverse("article-list")
        self.assertEqual(url, self.path)

    def test_detail(self):
        url = reverse("article-detail", kwargs={'slug': self.slug})
        self.assertEqual(url, self.path + self.slug + "/")


class CaseTests(TestCase):
    def setUp(self):
        self.path = "/cases/"
        self.slug = "some-slug"

    def test_list(self):
        url = reverse("case-list")
        self.assertEqual(url, self.path)

    def test_detail(self):
        url = reverse("case-detail", kwargs={'slug': self.slug})
        self.assertEqual(url, self.path + self.slug + "/")
