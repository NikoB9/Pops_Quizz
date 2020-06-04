from importlib import import_module

from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings as django_settings


from .set_db import set_db


from Quizz.views import *
from Quizz.requests.request_user import *
from Quizz.requests.request_game import *
from Quizz.requests.request_player import *

class SessionEnabledTestCase(TestCase):

    def get_session(self):
        if self.client.session:
            session = self.client.session
        else:
            engine = import_module(django_settings.SESSION_ENGINE)
            session = engine.SessionStore()
        return session

    def set_session_cookies(self, session):
        # Set the cookie to represent the session
        session_cookie = django_settings.SESSION_COOKIE_NAME
        self.client.cookies[session_cookie] = session.session_key
        cookie_data = {
            'max-age': None,
            'path': '/',
            'domain': django_settings.SESSION_COOKIE_DOMAIN,
            'secure': django_settings.SESSION_COOKIE_SECURE or None,
            'expires': None}
        self.client.cookies[session_cookie].update(cookie_data)

class Test_view(SessionEnabledTestCase):

    def setUp(self):
        set_db()
        session = self.get_session()
        session['login'] = 'Warren'
        session.save()
        self.set_session_cookies(session)
        self.game_warren = create_gameBD(1, "Warren", "Partie de Warren", False, 1, False, False, "DRAFT")

    def test_index(self):
        response = self.client.get(reverse('Quizz:home'))
        # self.assertEquals(str(response.context.get('user')), "Warren")
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(response.context.get('allforms').count(), 7)

    def test_quizz_by_cat(self):
        response = self.client.get(reverse('Quizz:show_cat', kwargs={'cat_id':1}))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context.get('cat').label, "Autre catégorie")

    def test_create_game(self):
        response = self.client.get(reverse('Quizz:create-game', kwargs={'id_form':1}))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context.get('game').name, "Partie de Warren")

    def test_attente(self):
        data = { 'game_name': self.game_warren.name, 'slot_max': self.game_warren.slot_max, 'is_public': self.game_warren.is_public}
        response = self.client.post(reverse('Quizz:attente', kwargs={'game_uuid':self.game_warren.uuid}), data)
        self.assertEquals(response.status_code, 200)

    def test_joindre_partie(self):
        response = self.client.get(reverse('Quizz:joindre-partie', kwargs={'game_uuid': self.game_warren.uuid}))
        self.assertEquals(response.status_code, 200)

    def test_retour_salon(self):
        response = self.client.get(reverse('Quizz:retour-salon'))
        self.assertEquals(response.status_code, 200)

    def test_quitter_partie(self):
        user = getUserByLogin("Warren")
        create_player(self.game_warren, user)
        response = self.client.get(reverse('Quizz:quitter-partie', kwargs={'game_uuid': self.game_warren.uuid}))
        self.assertEquals(response.status_code, 200)

    def test_openform(self):
        user = getUserByLogin("Warren")
        create_player(self.game_warren, user)
        response = self.client.get(reverse('Quizz:openform', kwargs={'game_uuid': self.game_warren.uuid}))
        self.assertEquals(response.status_code, 200)

    def test_users(self):
        response = self.client.get(reverse('Quizz:users'))
        self.assertEquals(response.status_code, 200)

    def test_create_user(self):
        data = { 'loginco': "abc", 'emailco': "abc@abc.com", 'passwordco': "abcabc", 'passwordco2': "abcabc"}
        response = self.client.post(reverse('Quizz:create_user'), data)
        self.assertEquals(response.status_code, 200)

    def test_connectUser(self):
        data = { 'login': "Warren", 'password': "wawa"}
        response = self.client.post(reverse('Quizz:connectUser'), data)
        self.assertEquals(response.status_code, 200)

    def test_disconnect(self):
        response = self.client.get(reverse('Quizz:disconnect'))
        self.assertEquals(response.status_code, 200)
