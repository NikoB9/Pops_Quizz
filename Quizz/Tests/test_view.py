from django.test import TestCase
from django.urls import reverse
from Quizz.views import *
from .set_db import set_db

class Test_view(TestCase):

    def setUp(self):
        set_db()

    def test_index(self):
        response = self.client.get(reverse('Quizz:home'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context.get('allforms').count(), 7)

    def test_display_form(self):
        response = self.client.get(reverse('Quizz:openform', kwargs={'idform':1}))
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(response.context.get('form').questions, 3)
