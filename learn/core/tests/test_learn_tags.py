from django.test import TestCase
import collections

from core.templatetags.learn_tags import get_item, sort


class SortTests(TestCase):
    def setUp(self):
        self.dict = {
            "10": "ten",
            "1": "one"
        }

    def test_sort(self):
        output = sort(self.dict.items())
        self.assertEqual(output[0], ('1', 'one'))


class GetItemTests(TestCase):
    def setUp(self):
        self.dict = {
            "10": "ten",
            "1": "one"
        }

    def test_get_item(self):
        output = get_item(self.dict, '1')
        self.assertEqual(output, 'one')