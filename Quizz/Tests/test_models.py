from django.test import TestCase

from Quizz.requests.request_answer_type import getType
from Quizz.requests.request_player import *
from Quizz.requests.request_user import *
from Quizz.requests.request_form import *
from Quizz.requests.request_question import *
from Quizz.requests.request_game import *
from .set_db import set_db


# coverage run --source='.' manage.py test

# MODIFIER UUID EN BASE POUR APPLIQUER PK

class Test_model(TestCase):

    def setUp(self):
        set_db()

    ## TEST ACCESS_FORM ##

    def test_get_access_form_from_form_and_user(self):
        form_1 = getFormById(1)
        user = getUserByLogin("Warren")
        self.assertEquals("CREATOR", return_highest_user_acces_to_form(user, form_1).access_form_type.type)

    ## TEST CATEGORIES ##

    def test_get_categories(self):
        categories = get_categories()
        self.assertEquals(1, len(categories))
        self.assertEquals("Autre catégorie", categories[0].label)

    ## TEST FORM ##

    def test_get_form(self):
        form_1 = getFormById(1)
        self.assertEquals(form_1.name, "Premier formulaire")

    def test_get_all_forms(self):
        forms = getAllForms()
        self.assertEquals(len(forms), 4)
        self.assertEquals(forms[0].name, "Premier formulaire")

    def test_add_quizz_form(self):
        forms = getAllForms()
        self.assertEquals(len(forms), 4)
        self.assertEquals(forms[0].name, "Premier formulaire")

        user = getUserByLogin("TimFake")
        categories = [get_category_by_label("Autre catégorie").id]
        addQuizzForm("new form", user, "new description", categories)
        forms = getAllForms()
        self.assertEquals(len(forms), 5)
        self.assertEquals(forms[4].name, "new form")

        self.assertEquals(True, is_a_user_allowed_to_access_a_form(user, forms[4]))

    def test_delete_form(self):
        forms = getAllForms()
        self.assertEquals(len(forms), 4)
        self.assertEquals(forms[0].name, "Premier formulaire")

        delete_form(forms[0].id)
        forms = getAllForms()
        self.assertEquals(len(forms), 3)

    def test_get_form_access(self):
        forms = getAllForms()
        self.assertEquals(len(forms), 4)
        self.assertEquals(forms[0].name, "Premier formulaire")

        user = getUserByLogin("TimFake")
        forms = getAllForms(user)
        self.assertEquals(len(forms), 3)
        self.assertEquals(forms[0].name, "Deuxième formulaire")

    def test_getAllFormsAccessUser(self):
        user = getUserByLogin("TimFake")
        forms = getAllFormsAccessUser(user)
        self.assertEquals(len(forms), 6)

    def test_nbQuizzByCat(self):
        cat = get_category_by_id(1)
        user = getUserByLogin("TimFake")
        self.assertEquals(1, nbQuizzByCat(cat))
        self.assertEquals(2, nbQuizzByCat(cat, user))

    ## TEST FRIENDS ##

    def test_two_users_have_relationship_true(self):
        userTim = getUserByLogin("TimFake")
        userAmi = getUserByLogin("copain du 31")
        self.assertEquals(True, two_users_have_relationship(userTim, userAmi))

    def test_two_users_have_relationship_false(self):
        userTim = getUserByLogin("TimFake")
        userSalome = getUserByLogin("SaloméFake")
        self.assertEquals(False, two_users_have_relationship(userTim, userSalome))

    def test_relationship_accepted_true(self):
        user = getUserByLogin("TimFake")
        userAmi = getUserByLogin("copain du 31")
        self.assertEquals(True, relationship_accepted(user, userAmi))

    def test_relationship_accepted_false(self):
        user = getUserByLogin("TimFake")
        userAttente = getUserByLogin("ami en demande")
        self.assertEquals(False, relationship_accepted(user, userAttente))

    def test_relationship_accept(self):
        user = getUserByLogin("TimFake")
        userAttente = getUserByLogin("ami en demande")
        self.assertEquals(False, relationship_accepted(user, userAttente))
        answer_friendship_request(True, user, userAttente)
        self.assertEquals(True, relationship_accepted(user, userAttente))

    def test_relationship_denied(self):
        user = getUserByLogin("TimFake")
        userAttente = getUserByLogin("ami en demande")
        self.assertEquals(False, relationship_accepted(user, userAttente))
        answer_friendship_request(False, user, userAttente)
        self.assertEquals(False, two_users_have_relationship(user, userAttente))

    def test_add_friend(self):
        user = getUserByLogin("TimFake")
        friends = get_waiting_sent_users_friend(user)
        self.assertEquals(1, len(friends))

        userSalome = getUserByLogin("SaloméFake")
        add_friend_request(user, userSalome)
        friends = get_waiting_sent_users_friend(user)
        self.assertEquals(2, len(friends))
        self.assertEquals("SaloméFake", friends[1].login)

    ## TEST GAME ##

    def test_get_all_Game(self):
        games = get_all_game()
        self.assertEquals(1, len(games))
        self.assertEquals("Game of Wawa on form 1", games[0].name)

    def test_get_game_uuid(self):
        uuid = get_all_game()[0].uuid
        game = get_game_by_uuid(uuid)
        self.assertEquals("Game of Wawa on form 1", game.name)
        self.assertEquals("WAITING", game.game_status.type)

    def test_change_game_status(self):
        game = get_all_game()[0]
        self.assertEquals("WAITING", game.game_status.type)
        change_game_status(game, "CANCELLED")
        games = get_all_game()
        self.assertEquals(1, len(games))
        self.assertEquals("CANCELLED", games[0].game_status.type)

    def test_edit_game(self):
        game = get_all_game()[0]
        self.assertEquals("Game of Wawa on form 1", game.name)
        self.assertEquals(1, game.slot_max)
        self.assertEquals(False, game.is_real_time)
        self.assertEquals(False, game.is_public)
        self.assertEquals("WAITING", game.game_status.type)

        game = edit_game(game.uuid, "new name", 10, True, True, True, timedelta(seconds=120))
        self.assertEquals("new name", game.name)
        self.assertEquals(10, game.slot_max)
        self.assertEquals(True, game.is_real_time)
        self.assertEquals(True, game.is_public)
        self.assertEquals("WAITING", game.game_status.type)

        game = edit_game(game.uuid, "new name", 10, True, True, False, 0, "DONE")
        self.assertEquals("DONE", game.game_status.type)

    def test_create_game(self):
        games = get_all_game()
        self.assertEquals(1, len(games))
        self.assertEquals("Game of Wawa on form 1", games[0].name)

        create_gameBD(1, "Warren", "Partie de Warren", True, 3, False)

        games = get_all_game()
        self.assertEquals(2, len(games))
        new_game = games[1]
        self.assertEquals(1, new_game.form.id)
        self.assertEquals("Partie de Warren", new_game.name)
        self.assertEquals(True, new_game.is_public)
        self.assertEquals(3, new_game.slot_max)


    ## TEST PLAYER ##

    def test_get_player_by_id(self):
        player = get_player_by_id(1)
        self.assertEquals("TimFake", player.user.login)
        self.assertEquals(True, player.has_answered)
        self.assertEquals(0, player.score)

    def test_calculate_score(self):
        game = get_all_game()[0]
        player = get_player_by_game_by_login(game, "TimFake")
        calculate_score(player)
        self.assertEquals(3, player.score)

    def test_create_delete_player(self):
        user = getUserByLogin("Warren")
        game = get_all_game()[0]
        self.assertEquals(False, is_user_in_game(user, game))
        create_player(game, user)
        self.assertEquals(True, is_user_in_game(user, game))
        user_leave_game(user, game)
        self.assertEquals(False, is_user_in_game(user, game))

    def test_player_number_of_game(self):
        game = get_all_game()[0]
        player_parties = get_players_number_of_game(get_players_by_game(game))
        self.assertEquals(1, player_parties[0].parties)

    def test_get_nb_player_by_game(self):
        game = get_all_game()[0]
        self.assertEquals(1, get_nb_player_by_game(game))


    ## TEST QUESTION ##
    def test_get_question_by_form_id(self):
        form_1 = getFormById(1)
        questions = getQuestionsByForm(form_1)
        self.assertEquals(3, len(questions))
        first_question = questions[0]
        self.assertEquals(form_1, first_question.form)
        self.assertEquals("QCM", first_question.answer_type.type)
        self.assertEquals("première question", first_question.label)
        self.assertEquals(1, first_question.order)

    def test_add_question(self):
        form_1 = getFormById(1)
        questions = getQuestionsByForm(form_1)
        self.assertEquals(3, len(questions))
        first_question = questions[0]
        self.assertEquals(form_1, first_question.form)
        self.assertEquals("QCM", first_question.answer_type.type)
        self.assertEquals("première question", first_question.label)
        self.assertEquals(1, first_question.order)

        addQuestion(form_1, getType("INPUT"), "new question", 4)

        questions = getQuestionsByForm(form_1)
        self.assertEquals(4, len(questions))
        first_question = questions[0]
        self.assertEquals(form_1, first_question.form)
        self.assertEquals("QCM", first_question.answer_type.type)
        self.assertEquals("première question", first_question.label)
        self.assertEquals(1, first_question.order)
        last_question = questions[3]
        self.assertEquals(form_1, last_question.form)
        self.assertEquals("INPUT", last_question.answer_type.type)
        self.assertEquals("new question", last_question.label)
        self.assertEquals(4, last_question.order)

    def test_possible_answer_by_questions(self):
        form_1 = getFormById(1)
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

    def test_user_possible_answer_by_questions(self):
        form_1 = getFormById(1)
        player = get_player_by_id(1)
        questions = getQuestionsByForm(form_1)
        question_by_possible_answers = getUserAnswersByQuestions(questions, player)
        self.assertEquals(3, len(question_by_possible_answers))
        possible_answers_of_first_question = question_by_possible_answers[0]["answers"]
        self.assertEquals(2, len(possible_answers_of_first_question))
        self.assertEquals(False, possible_answers_of_first_question[0].correct)
        self.assertEquals("1", possible_answers_of_first_question[0].value)
        self.assertEquals(True, possible_answers_of_first_question[1].correct)
        self.assertEquals("2", possible_answers_of_first_question[1].value)
        self.assertEquals("1", possible_answers_of_first_question[1].ua.value)

        possible_answers_of_second_question = question_by_possible_answers[1]["answers"]
        self.assertEquals(2, len(possible_answers_of_second_question))
        self.assertEquals(False, possible_answers_of_second_question[0].correct)
        self.assertEquals("1", possible_answers_of_second_question[0].value)
        self.assertEquals(True, possible_answers_of_second_question[1].correct)
        self.assertEquals("2", possible_answers_of_second_question[1].value)
        self.assertEquals("4", possible_answers_of_second_question[1].ua.value)

        possible_answers_of_third_question = question_by_possible_answers[2]["answers"]
        self.assertEquals(True, question_by_possible_answers[2]["question"].input_valide)
        self.assertEquals(1, len(possible_answers_of_third_question))
        self.assertEquals(True, possible_answers_of_third_question[0].correct)
        self.assertEquals("texte", possible_answers_of_third_question[0].value)
        self.assertEquals("texte", possible_answers_of_third_question[0].ua.value)

    ## TEST POSSIBLE_ANSWER ##

    def test_create_possible_answer(self):
        form_1 = getFormById(1)
        question = getQuestionsByForm(form_1)[0]
        pa = get_possible_answer_of_a_question(question)
        self.assertEquals(2, len(pa))

        addPossibleAnswer(question, True, "3")

        pa = get_possible_answer_of_a_question(question)
        self.assertEquals(3, len(pa))

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

    def test_edit_user(self):
        user = getUserByLogin("TimFake")
        self.assertEquals("TimFake", user.login)
        self.assertEquals("tony.lim@u-psud.fr", user.mail)

        editUserWithoutPwd(user.id, "new login", "new.mail@mail.com")

        new_user = getUserByLogin("new login")
        self.assertEquals(user.id, new_user.id)
        self.assertEquals("new login", new_user.login)
        self.assertEquals("new.mail@mail.com", new_user.mail)

    def test_login_exist(self):
        self.assertEquals(False, loginExist("new.user@mail.com"))
        createUserBD("new user", "new.user@mail.com", "new password")
        self.assertEquals(True, loginExist("new user"))

    def test_mail_exist(self):
        self.assertEquals(False, emailExist("new.user@mail.com"))
        createUserBD("new user", "new.user@mail.com", "new password")
        self.assertEquals(True, emailExist("new.user@mail.com"))

    def test_user_exist(self):
        self.assertEquals(False, valideUser("TimFake", "titi"))
        self.assertEquals(True, valideUser("TimFake", "toto"))

    def test_get_users_friends(self):
        user = getUserByLogin("TimFake")
        friends = get_users_friends(user)
        self.assertEquals(1, len(friends))
        self.assertEquals("copain du 31", friends[0].login)

    def test_get_waiting_sent_users_friend(self):
        user = getUserByLogin("TimFake")
        friends = get_waiting_sent_users_friend(user)
        self.assertEquals(1, len(friends))
        self.assertEquals("ami absent", friends[0].login)

    def test_get_waiting_received_users_friend(self):
        user = getUserByLogin("TimFake")
        friends = get_waiting_received_users_friend(user)
        self.assertEquals(1, len(friends))
        self.assertEquals("ami en demande", friends[0].login)

    def test_good_bad_answer(self):
        user = getUserByLogin("TimFake")
        self.assertEquals(0, user.good_answer)
        self.assertEquals(0, user.bad_answer)

        user_add_good_answer(user)
        user_add_bad_answer(user)

        self.assertEquals(1, user.good_answer)
        self.assertEquals(1, user.bad_answer)

    def test_get_n_first_users_like_with_a_user_to_exclude(self):
        user = getUserByLogin("TimFake")
        users = get_n_first_users_like_with_a_user_to_exclude("fake", user)
        self.assertEquals(3, len(users))
        self.assertEquals("NicoFake", users[0].login)
        self.assertEquals("SaloméFake", users[1].login)
        self.assertEquals("WiirioFake", users[2].login)

