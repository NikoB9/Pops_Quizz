from django.test import TestCase

from Quizz.requests.request_answer_type import getType
from Quizz.requests.request_player import *
from Quizz.requests.request_user import *
from Quizz.requests.request_form import *
from Quizz.requests.request_question import *
from Quizz.requests.request_game import *


# MODIFIER UUID EN BASE POUR APPLIQUER PK

class Test_model(TestCase):

    def setUp(self):
        gameStatusCancelled = GameStatus()
        gameStatusCancelled.type = "CANCELLED"
        gameStatusCancelled.save()

        gameStatusWaiting = GameStatus()
        gameStatusWaiting.type = "WAITING"
        gameStatusWaiting.save()

        gameStatusDone = GameStatus()
        gameStatusDone.type = "DONE"
        gameStatusDone.save()

        gameStatusInProgress = GameStatus()
        gameStatusInProgress.type = "IN_PROGRESS"
        gameStatusInProgress.save()

        userWawa = User()
        userWawa.login = "Warren"
        userWawa.mail = "warren.weber@hotmail.fr"
        userWawa.password = hashers.make_password("wawa")
        userWawa.save()

        userTony = User()
        userTony.login = "TimFake"
        userTony.mail = "tony.lim@u-psud.fr"
        userTony.password = hashers.make_password("toto")
        userTony.save()

        userNico = User()
        userNico.login = "NicoFake"
        userNico.mail = "nico@wanadoo.com"
        userNico.password = hashers.make_password("djangogo")
        userNico.save()

        userSalome = User()
        userSalome.login = "SaloméFake"
        userSalome.mail = "salomette@yahoo.fr"
        userSalome.password = hashers.make_password("jaimelecss")
        userSalome.save()

        userThibaut = User()
        userThibaut.login = "WiirioFake"
        userThibaut.mail = "thibaut@aol.fr"
        userThibaut.password = hashers.make_password("test")
        userThibaut.save()

        userAmi = User()
        userAmi.login = "copain du 31"
        userAmi.mail = "ami@aol.fr"
        userAmi.password = hashers.make_password("jaime")
        userAmi.save()

        userAmiAttente = User()
        userAmiAttente.login = "ami en demande"
        userAmiAttente.mail = "chercheami@gmail.com"
        userAmiAttente.password = hashers.make_password("demande")
        userAmiAttente.save()

        userGhost = User()
        userGhost.login = "ami absent"
        userGhost.mail = "amiperdu@gmail.com"
        userGhost.password = hashers.make_password("ghost")
        userGhost.save()

        relationAmiTony = Friends()
        relationAmiTony.accepted = True
        relationAmiTony.source = userAmi
        relationAmiTony.target = userTony
        relationAmiTony.comment = "Accepte moi Tony !"
        relationAmiTony.save()

        relationAmiNico = Friends()
        relationAmiNico.accepted = True
        relationAmiNico.source = userAmi
        relationAmiNico.target = userNico
        relationAmiNico.comment = "Accepte moi stp Nico"
        relationAmiNico.save()

        relationAmiSalome = Friends()
        relationAmiSalome.accepted = True
        relationAmiSalome.source = userAmi
        relationAmiSalome.target = userSalome
        relationAmiSalome.comment = "On devient ami Salomette ?"
        relationAmiSalome.save()

        relationAmiWarren = Friends()
        relationAmiWarren.accepted = True
        relationAmiWarren.source = userAmi
        relationAmiWarren.target = userWawa
        relationAmiWarren.comment = "On devient ami Wawa ?"
        relationAmiWarren.save()

        relationAmiThibaut = Friends()
        relationAmiThibaut.accepted = True
        relationAmiThibaut.source = userAmi
        relationAmiThibaut.target = userThibaut
        relationAmiThibaut.comment = "On devient ami Thibaut ?"
        relationAmiThibaut.save()

        relationAmiTony = Friends()
        relationAmiTony.accepted = True
        relationAmiTony.source = userAmiAttente
        relationAmiTony.target = userTony
        relationAmiTony.comment = "Accepte moi Tony !"
        relationAmiTony.save()

        relationAmiNico = Friends()
        relationAmiNico.accepted = True
        relationAmiNico.source = userAmiAttente
        relationAmiNico.target = userNico
        relationAmiNico.comment = "Accepte moi stp Nico"
        relationAmiNico.save()

        relationAmiSalome = Friends()
        relationAmiSalome.accepted = True
        relationAmiSalome.source = userAmiAttente
        relationAmiSalome.target = userSalome
        relationAmiSalome.comment = "On devient ami Salomette ?"
        relationAmiSalome.save()

        relationAmiWarren = Friends()
        relationAmiWarren.accepted = True
        relationAmiWarren.source = userAmiAttente
        relationAmiWarren.target = userWawa
        relationAmiWarren.comment = "On devient ami Wawa ?"
        relationAmiWarren.save()

        relationAmiThibaut = Friends()
        relationAmiThibaut.accepted = True
        relationAmiThibaut.source = userAmiAttente
        relationAmiThibaut.target = userThibaut
        relationAmiThibaut.comment = "On devient ami Thibaut ?"
        relationAmiThibaut.save()

        relationAttenteTony = Friends()
        relationAttenteTony.accepted = False
        relationAttenteTony.source = userAmiAttente
        relationAttenteTony.target = userTony
        relationAttenteTony.comment = "Accepte moi Tony !"
        relationAttenteTony.save()

        relationAttenteNico = Friends()
        relationAttenteNico.accepted = False
        relationAttenteNico.source = userAmiAttente
        relationAttenteNico.target = userNico
        relationAttenteNico.comment = "Accepte moi stp Nico"
        relationAttenteNico.save()

        relationAttenteSalome = Friends()
        relationAttenteSalome.accepted = False
        relationAttenteSalome.source = userAmiAttente
        relationAttenteSalome.target = userSalome
        relationAttenteSalome.comment = "On devient ami Salomette ?"
        relationAttenteSalome.save()

        relationAttenteWarren = Friends()
        relationAttenteWarren.accepted = False
        relationAttenteWarren.source = userAmiAttente
        relationAttenteWarren.target = userWawa
        relationAttenteWarren.comment = "On devient ami Wawa ?"
        relationAttenteWarren.save()

        relationAttenteThibaut = Friends()
        relationAttenteThibaut.accepted = False
        relationAttenteThibaut.source = userAmiAttente
        relationAttenteThibaut.target = userThibaut
        relationAttenteThibaut.comment = "On devient ami Thibaut ?"
        relationAttenteThibaut.save()

        relationGhostTony = Friends()
        relationGhostTony.accepted = False
        relationGhostTony.target = userGhost
        relationGhostTony.source = userTony
        relationGhostTony.comment = "Accepte moi Tony !"
        relationGhostTony.save()

        relationGhostNico = Friends()
        relationGhostNico.accepted = False
        relationGhostNico.target = userGhost
        relationGhostNico.source = userNico
        relationGhostNico.comment = "Accepte moi stp Nico"
        relationGhostNico.save()

        relationGhostSalome = Friends()
        relationGhostSalome.accepted = False
        relationGhostSalome.target = userGhost
        relationGhostSalome.source = userSalome
        relationGhostSalome.comment = "On devient ami Salomette ?"
        relationGhostSalome.save()

        relationGhostWarren = Friends()
        relationGhostWarren.accepted = False
        relationGhostWarren.target = userGhost
        relationGhostWarren.source = userWawa
        relationGhostWarren.comment = "On devient ami Wawa ?"
        relationGhostWarren.save()

        relationGhostThibaut = Friends()
        relationGhostThibaut.accepted = False
        relationGhostThibaut.target = userGhost
        relationGhostThibaut.source = userThibaut
        relationGhostThibaut.comment = "On devient ami Thibaut ?"
        relationGhostThibaut.save()

        accessFormTypeCreator = AccessFormType()
        accessFormTypeCreator.type = "CREATOR"
        accessFormTypeCreator.save()
        accessFormTypeEditor = AccessFormType()
        accessFormTypeCreator.type = "EDITOR"
        accessFormTypeEditor.save()
        accessFormTypePublisher = AccessFormType()
        accessFormTypeCreator.type = "PUBLISHER"
        accessFormTypePublisher.save()

        f = Form()
        f.name = "Premier formulaire"
        f.description = "C'est parti !"
        f.author = userWawa
        f.is_public = True
        f.save()

        AF1 = AccessForm()
        AF1.form = f
        AF1.user = userWawa
        AF1.access_form_type = accessFormTypeCreator
        AF1.save()

        game = Game()
        game.slot_max = 1
        game.author = userWawa
        game.form = f
        game.is_public = False
        game.name = "Game of Wawa on form 1"
        game.uuid = str(uuid.uuid4())[:8]
        game.game_status = gameStatusWaiting
        game.save()

        player1 = Player()
        player1.user = userTony
        player1.game = game
        player1.has_answered = 1
        player1.score = 0
        player1.save()

        qcmType = AnswerType()
        qcmType.type = "QCM"
        qcmType.save()

        inputType = AnswerType()
        inputType.type = "INPUT"
        inputType.save()

        uniqueAnswerType = AnswerType()
        uniqueAnswerType.type = "UNIQUE_ANSWER"
        uniqueAnswerType.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answer_type = qcmType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        ua1 = UserAnswers()
        ua1.player = player1
        ua1.possible_answer = pa
        ua1.value = 1
        ua1.save()

        question = Question()
        question.form = f
        question.label = "deuxième question"
        question.order = 2
        question.answer_type = uniqueAnswerType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        ua2 = UserAnswers()
        ua2.player = player1
        ua2.possible_answer = pa
        ua2.value = 4
        ua2.save()

        question = Question()
        question.form = f
        question.label = "troisième question"
        question.order = 3
        question.answer_type = inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value = "texte"
        possAnswer.correct = True
        possAnswer.save()

        ua3 = UserAnswers()
        ua3.player = player1
        ua3.possible_answer = possAnswer
        ua3.value = "texte"
        ua3.save()

        ####################################

        f = Form()
        f.name = "Deuxième formulaire"
        f.description = "C'est parti !"
        f.author = userTony
        f.is_public = False
        f.save()
        AF2 = AccessForm()
        AF2.form = f
        AF2.user = f.author
        AF2.access_form_type = accessFormTypeCreator
        AF2.save()

        AF2Wawa = AccessForm()
        AF2Wawa.form = f
        AF2Wawa.user = userWawa
        AF2Wawa.access_form_type = accessFormTypeEditor
        AF2Wawa.save()

        AF2Thibaut = AccessForm()
        AF2Thibaut.form = f
        AF2Thibaut.user = userThibaut
        AF2Thibaut.access_form_type = accessFormTypeEditor
        AF2Thibaut.save()

        AF2Nico = AccessForm()
        AF2Nico.form = f
        AF2Nico.user = userNico
        AF2Nico.access_form_type = accessFormTypeEditor
        AF2Nico.save()

        AF2Salome = AccessForm()
        AF2Salome.form = f
        AF2Salome.user = userSalome
        AF2Salome.access_form_type = accessFormTypeEditor
        AF2Salome.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answer_type = qcmType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "deuxième question"
        question.order = 2
        question.answer_type = uniqueAnswerType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "troisième question"
        question.order = 3
        question.answer_type = inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value = "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Troisième formulaire"
        f.description = "C'est parti !"
        f.author = userTony
        f.is_public = True
        f.save()
        AF3 = AccessForm()
        AF3.form = f
        AF3.user = f.author
        AF3.access_form_type = accessFormTypeCreator
        AF3.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answer_type = qcmType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "deuxième question"
        question.order = 2
        question.answer_type = uniqueAnswerType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "troisième question"
        question.order = 3
        question.answer_type = inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value = "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Quatrième formulaire"
        f.description = "C'est parti !"
        f.author = userNico
        f.is_public = True
        f.save()
        AF4 = AccessForm()
        AF4.form = f
        AF4.user = f.author
        AF4.access_form_type = accessFormTypeCreator
        AF4.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answer_type = qcmType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "deuxième question"
        question.order = 2
        question.answer_type = uniqueAnswerType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "troisième question"
        question.order = 3
        question.answer_type = inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value = "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Cinquième formulaire"
        f.description = "C'est parti !"
        f.author = userThibaut
        f.is_public = True
        f.save()
        AF5 = AccessForm()
        AF5.form = f
        AF5.user = f.author
        AF5.access_form_type = accessFormTypeCreator
        AF5.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answer_type = qcmType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "deuxième question"
        question.order = 2
        question.answer_type = uniqueAnswerType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "troisième question"
        question.order = 3
        question.answer_type = inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value = "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Sixième formulaire"
        f.description = "C'est parti !"
        f.author = userSalome
        f.is_public = True
        f.save()
        AF6 = AccessForm()
        AF6.form = f
        AF6.user = f.author
        AF6.access_form_type = accessFormTypeCreator
        AF6.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answer_type = qcmType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "deuxième question"
        question.order = 2
        question.answer_type = uniqueAnswerType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "troisième question"
        question.order = 3
        question.answer_type = inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value = "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Septième formulaire"
        f.description = "C'est parti !"
        f.author = userTony
        f.is_public = False
        f.save()
        AF7 = AccessForm()
        AF7.form = f
        AF7.user = f.author
        AF7.access_form_type = accessFormTypeCreator
        AF7.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answer_type = qcmType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "deuxième question"
        question.order = 2
        question.answer_type = uniqueAnswerType
        question.save()

        pa = PossibleAnswer()
        pa.value = "1"
        pa.question = question
        pa.correct = False
        pa.save()

        pa = PossibleAnswer()
        pa.value = "2"
        pa.question = question
        pa.correct = True
        pa.save()

        question = Question()
        question.form = f
        question.label = "troisième question"
        question.order = 3
        question.answer_type = inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value = "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

    ## TEST ACCESS_FORM ##

    def test_get_access_form_from_form_and_user(self):
        form_1 = getFormById(1)
        user = getUserByLogin("Warren")
        self.assertEquals("CREATOR", return_highest_user_acces_to_form(user, form_1))

    ## TEST FORM ##

    def test_get_form(self):
        form_1 = getFormById(1)
        self.assertEquals(form_1.name, "Premier formulaire")

    def test_get_all_forms(self):
        forms = getAllForms()
        self.assertEquals(len(forms), 5)
        self.assertEquals(forms[0].name, "Premier formulaire")

    def test_add_quizz_form(self):
        forms = getAllForms()
        self.assertEquals(len(forms), 5)
        self.assertEquals(forms[0].name, "Premier formulaire")

        user = getUserByLogin("TimFake")
        addQuizzForm("new form", user, "new description")
        forms = getAllForms()
        self.assertEquals(len(forms), 6)
        self.assertEquals(forms[5].name, "new form")

        self.assertEquals(True, is_a_user_allowed_to_access_a_form(user, forms[5]))

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

        editUserBD(user.id, "new login", "new.mail@mail.com", None)

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
