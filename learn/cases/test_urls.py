from django.test import TestCase
from django.core.urlresolvers import reverse


class CaseTests(TestCase):
    def setUp(self):
        self.path = "/cases/"
        self.slug = "some-slug"

    def test_list(self):
        url = reverse("case-archive")
        self.assertEqual(url, self.path)

    def test_detail(self):
        url = reverse("case-detail", kwargs={'slug': self.slug})
        self.assertEqual(url, self.path + self.slug + "/")
