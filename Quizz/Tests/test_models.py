from django.test import TestCase
from Quizz.requests.request_user import *
from Quizz.requests.request_form import *
from Quizz.requests.request_question import *
from Quizz.requests.request_game import *
from .set_db import set_db

class Test_model(TestCase):

    def setUp(self):
        set_db()

    ## TEST FORM ##

    def test_get_form(self):
        form_1 = getFormsById(1)
        self.assertEquals(form_1.name, "Premier formulaire")

    def test_get_all_forms(self):
        forms = getAllForms()
        self.assertEquals(len(forms), 7)
        self.assertEquals(forms[0].name, "Premier formulaire")

    ## TEST QUESTION ##
    def test_get_question_by_form_id(self):
        form_1 = getFormsById(1)
        questions = getQuestionsByForm(form_1)
        self.assertEquals(3, len(questions))
        first_question = questions[0]
        self.assertEquals(form_1, first_question.form)
        self.assertEquals("QCM", first_question.answer_type.type)
        self.assertEquals("première question", first_question.label)
        self.assertEquals(1, first_question.order)

    def test_possible_answer_by_questions(self):
        form_1 = getFormsById(1)
        questions = getQuestionsByForm(form_1)
        question_by_possible_answers = getPossibleAnswersByQuestions(questions)
        self.assertEquals(3, len(question_by_possible_answers))
        possible_answers_of_first_question = question_by_possible_answers[0]["answers"]
        self.assertEquals(2, len(possible_answers_of_first_question))
        self.assertEquals(False, possible_answers_of_first_question[0].correct)
        self.assertEquals("1", possible_answers_of_first_question[0].value)
        self.assertEquals(True, possible_answers_of_first_question[1].correct)
        self.assertEquals("2", possible_answers_of_first_question[1].value)

        possible_answers_of_second_question = question_by_possible_answers[1]["answers"]
        self.assertEquals(2, len(possible_answers_of_second_question))
        self.assertEquals(False, possible_answers_of_second_question[0].correct)
        self.assertEquals("1", possible_answers_of_second_question[0].value)
        self.assertEquals(True, possible_answers_of_second_question[1].correct)
        self.assertEquals("2", possible_answers_of_second_question[1].value)

        possible_answers_of_third_question = question_by_possible_answers[2]["answers"]
        self.assertEquals(1, len(possible_answers_of_third_question))
        self.assertEquals(True, possible_answers_of_third_question[0].correct)
        self.assertEquals("texte", possible_answers_of_third_question[0].value)

    ## TEST USER ##

    def test_get_User_by_login(self):
        user = getUserByLogin("Warren")
        self.assertEquals("Warren", user.login)

    def test_get_all_Users(self):
        users = getAllUsers()
        self.assertEquals(8, len(users))
        self.assertEquals("Warren", users[0].login)

    def test_create_User(self):
        users = getAllUsers()
        self.assertEquals(8, len(users))
        createUserBD("new user", "new.user@mail.com", "new password")

        users = getAllUsers()
        self.assertEquals(9, len(users))
        newUser = users[8]
        self.assertEquals("new user", newUser.login)
        self.assertEquals("new.user@mail.com", newUser.mail)

    ## TEST GAME ##

    def test_get_all_Game(self):
        games = get_all_game()
        self.assertEquals(1, len(games))
        self.assertEquals("Game of Wawa on form 1", games[0].name)

    def test_create_game(self):
        games = get_all_game()
        self.assertEquals(1, len(games))
        self.assertEquals("Game of Wawa on form 1", games[0].name)

        #TODO complete test
