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
        data = {
                'game_name': self.game_warren.name,
                'slot_max': self.game_warren.slot_max,
                'is_public': self.game_warren.is_public
                }
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
        data = {
                'loginco': "abc",
                'emailco': "abc@abc.com",
                'passwordco': "abcabc",
                'passwordco2': "abcabc"
                }
        response = self.client.post(reverse('Quizz:create_user'), data)
        self.assertEquals(response.status_code, 200)

    def test_connectUser(self):
        data = { 'login': "Warren", 'password': "wawa"}
        response = self.client.post(reverse('Quizz:connectUser'), data)
        self.assertEquals(response.status_code, 200)

    def test_disconnect(self):
        response = self.client.get(reverse('Quizz:disconnect'))
        self.assertEquals(response.status_code, 200)

    def test_creation_post(self):
        data = {
                'form_title': "Test",
                'form_description': "Test",
                'category_list': "",
                'nbQuestions': "3",
                'qst_1_title': "Test question 1 radio",
                'qst_1_answerType': "radio",
                'qst_1_order': "1",
                'qst_1_nbAnswers': "2",
                'qst_1_ans_1_value': "A",
                'qst_1_ans_2_value': "B",
                'qst_1_ans_1_correct': "on",
                'qst_1_ans_2_correct': "off",

                'qst_2_title': "Test question 2 checkbox",
                'qst_2_answerType': "checkbox",
                'qst_2_order': "2",
                'qst_2_nbAnswers': "3",
                'qst_2_ans_1_value': "A",
                'qst_2_ans_2_value': "B",
                'qst_2_ans_3_value': "C",
                'qst_2_ans_1_correct': "on",
                'qst_2_ans_2_correct': "on",
                'qst_2_ans_3_correct': "off",

                'qst_3_title': "Test question 3 text",
                'qst_3_answerType': "text",
                'qst_3_order': "3",
                'qst_3_nbAnswers': "1",
                'qst_3_ans_1_value': "A",
                }
        response = self.client.post(reverse('Quizz:creation'), data)
        self.assertEquals(response.status_code, 200)

    def test_creation_get(self):
        response = self.client.get(reverse('Quizz:creation'))
        self.assertEquals(response.status_code, 200)

    def test_edit_quizz(self):
        response = self.client.get(reverse('Quizz:edit_quizz', kwargs={'id_quizz': 1}))
        self.assertEquals(response.status_code, 200)

    def test_delete_quizz(self):
        response = self.client.get(reverse('Quizz:delete_quizz', kwargs={'id_quizz': 1}))
        self.assertEquals(response.status_code, 200)

    def test_saveUserAnswers_QCM(self):
        data = {
                'idplayer': "1",
                'idPA': "2",
                'value': "2",
                }
        response = self.client.post(reverse('Quizz:save_user_answers'), data)
        self.assertEquals(response.status_code, 200)

    def test_saveUserAnswers_UNIQUE_ANSWERS(self):
        data = {
                'idplayer': "1",
                'idPA': "4",
                'value': "2",
                }
        response = self.client.post(reverse('Quizz:save_user_answers'), data)
        self.assertEquals(response.status_code, 200)

    def test_change_user_invite(self):
        pass

    def test_remove_friend(self):
        pass

    def test_add_friend(self):
        pass

    def test_invite_friend(self):
        pass

    def test_user_profil(self):
        pass

    def test_user_history(self):
        response = self.client.get(reverse('Quizz:dashboard_history'))
        self.assertEquals(response.status_code, 200)

    def test_correction(self):
        response = self.client.get(reverse('Quizz:correction', kwargs={'player_id': 1}))
        self.assertEquals(response.status_code, 200)

    def test_menuCategories(self):
        response = self.client.get(reverse('Quizz:menuCategories'))
        self.assertEquals(response.status_code, 200)

    def test_stats(self):
        response = self.client.get(reverse('Quizz:dashboard_stats'))
        self.assertEquals(response.status_code, 200)

    def test_amis(self):
        response = self.client.get(reverse('Quizz:dashboard_friend'))
        self.assertEquals(response.status_code, 200)
