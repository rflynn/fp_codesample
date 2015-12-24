from django.db.models.manager import Manager
from django.test import TestCase
from mock import patch, Mock, MagicMock

from msg.models import Messages


class TestMessages0(TestCase):
    def setUp(self):
        pass
    def test_count(self):
        self.assertEqual(0, Messages.count_cities())

class TestMessages1(TestCase):
    def setUp(self):
        Messages(username='_', city='A', state='_').save()
    def test_count(self):
        self.assertEqual(1, Messages.count_cities())

class TestMessages1b(TestCase):
    def setUp(self):
        Messages(username='_', city='A', state='_').save()
        Messages(username='_', city='A', state='_').save()
    def test_count(self):
        self.assertEqual(1, Messages.count_cities())

class TestMessages2(TestCase):
    def setUp(self):
        Messages(username='_', city='A', state='_').save()
        Messages(username='_', city='B', state='_').save()
    def test_count(self):
        self.assertEqual(2, Messages.count_cities())
