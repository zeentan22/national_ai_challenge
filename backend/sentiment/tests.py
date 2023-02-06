from django.test import TestCase
from .models import History, Data

class HistoryTestCase(TestCase):
    def setUp(self):
        History.objects.create(user_input="The food was good, price was ok, service was bad.")