from django.test import TestCase
from django.urls import reverse
from Quizz.views import *
from .set_db import set_db

class Test_view(TestCase):

    def setUp(self):
        set_db()

    def test_index(self):
        # self.client.login(username = "Warren", password = hashers.make_password("wawa"))
        response = self.client.get(reverse('Quizz:home'))
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(response.context.get('allforms').count(), 7)

    def test_create_game(self):
        # self.client.login(username = "Warren", password = "wawa")
        response = self.client.get(reverse('Quizz:create-game', kwargs={'id_form':1}))
        # self.assertEquals(str(response.context.get('user')), "Warren")
        self.assertEquals(response.status_code, 200)
