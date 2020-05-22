from django.test import TestCase
from Quizz.requests.request_user import *
from Quizz.requests.request_form import *
from Quizz.requests.request_question import *

class Test_model(TestCase):

    def setUp(self):

        userWawa = User()
        userWawa.login="Warren"
        userWawa.mail="warren.weber@hotmail.fr"
        userWawa.password="wawa"
        userWawa.save()

        userTony = User()
        userTony.login="TimFake"
        userTony.mail="tony.lim@u-psud.fr"
        userTony.password="toto"
        userTony.save()

        userNico = User()
        userNico.login="NicoFake"
        userNico.mail="nico@wanadoo.com"
        userNico.password="djangogo"
        userNico.save()

        userSalome = User()
        userSalome.login="SaloméFake"
        userSalome.mail="salomette@yahoo.fr"
        userSalome.password="jaimelecss"
        userSalome.save()

        userThibaut = User()
        userThibaut.login="WiirioFake"
        userThibaut.mail="thibaut@aol.fr"
        userThibaut.password="test"
        userThibaut.save()

        userAmi = User()
        userAmi.login="copain du 31"
        userAmi.mail="ami@aol.fr"
        userAmi.password="jaime"
        userAmi.save()

        userAmiAttente = User()
        userAmiAttente.login="ami en demande"
        userAmiAttente.mail="chercheami@gmail.com"
        userAmiAttente.password="demande"
        userAmiAttente.save()

        userGhost = User()
        userGhost.login="ami absent"
        userGhost.mail="amiperdu@gmail.com"
        userGhost.password="ghost"
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
        accessFormTypeCreator.type="CREATOR"
        accessFormTypeCreator.save()
        accessFormTypeEditor = AccessFormType()
        accessFormTypeCreator.type="EDITOR"
        accessFormTypeEditor.save()
        accessFormTypePublisher = AccessFormType()
        accessFormTypeCreator.type="PUBLISHER"
        accessFormTypePublisher.save()

        f = Form()
        f.name = "Premier formulaire"
        f.description = "C'est parti !"
        f.author = userWawa
        f.isPublic = True
        f.save()

        AF1 = AccessForm()
        AF1.form = f
        AF1.user = userWawa
        AF1.accessFormType = accessFormTypeCreator
        AF1.save()


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
        question.answerType= qcmType
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
        question.answerType= uniqueAnswerType
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
        question.answerType= inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value= "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Deuxième formulaire"
        f.description = "C'est parti !"
        f.author = userTony
        f.isPublic = False
        f.save()
        AF2 = AccessForm()
        AF2.form = f
        AF2.user = f.author
        AF2.accessFormType = accessFormTypeCreator
        AF2.save()

        AF2Wawa = AccessForm()
        AF2Wawa.form = f
        AF2Wawa.user = userWawa
        AF2Wawa.accessFormType = accessFormTypeEditor
        AF2Wawa.save()

        AF2Thibaut = AccessForm()
        AF2Thibaut.form = f
        AF2Thibaut.user = userThibaut
        AF2Thibaut.accessFormType = accessFormTypeEditor
        AF2Thibaut.save()

        AF2Nico = AccessForm()
        AF2Nico.form = f
        AF2Nico.user = userNico
        AF2Nico.accessFormType = accessFormTypeEditor
        AF2Nico.save()

        AF2Salome = AccessForm()
        AF2Salome.form = f
        AF2Salome.user = userSalome
        AF2Salome.accessFormType = accessFormTypeEditor
        AF2Salome.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answerType= qcmType
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
        question.answerType= uniqueAnswerType
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
        question.answerType= inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value= "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Troisième formulaire"
        f.description = "C'est parti !"
        f.author = userTony
        f.isPublic = True
        f.save()
        AF3 = AccessForm()
        AF3.form = f
        AF3.user = f.author
        AF3.accessFormType = accessFormTypeCreator
        AF3.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answerType= qcmType
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
        question.answerType= uniqueAnswerType
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
        question.answerType= inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value= "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Quatrième formulaire"
        f.description = "C'est parti !"
        f.author = userNico
        f.isPublic = True
        f.save()
        AF4 = AccessForm()
        AF4.form = f
        AF4.user = f.author
        AF4.accessFormType = accessFormTypeCreator
        AF4.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answerType= qcmType
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
        question.answerType= uniqueAnswerType
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
        question.answerType= inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value= "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Cinquième formulaire"
        f.description = "C'est parti !"
        f.author = userThibaut
        f.isPublic = True
        f.save()
        AF5 = AccessForm()
        AF5.form = f
        AF5.user = f.author
        AF5.accessFormType = accessFormTypeCreator
        AF5.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answerType= qcmType
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
        question.answerType= uniqueAnswerType
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
        question.answerType= inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value= "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Sixième formulaire"
        f.description = "C'est parti !"
        f.author = userSalome
        f.isPublic = True
        f.save()
        AF6 = AccessForm()
        AF6.form = f
        AF6.user = f.author
        AF6.accessFormType = accessFormTypeCreator
        AF6.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answerType= qcmType
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
        question.answerType= uniqueAnswerType
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
        question.answerType= inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value= "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

        f = Form()
        f.name = "Septième formulaire"
        f.description = "C'est parti !"
        f.author = userTony
        f.isPublic = False
        f.save()
        AF7 = AccessForm()
        AF7.form = f
        AF7.user = f.author
        AF7.accessFormType = accessFormTypeCreator
        AF7.save()

        question = Question()
        question.form = f
        question.label = "première question"
        question.order = 1
        question.answerType= qcmType
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
        question.answerType= uniqueAnswerType
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
        question.answerType= inputType
        question.save()

        possAnswer = PossibleAnswer()
        possAnswer.question = question
        possAnswer.value= "texte"
        possAnswer.correct = True
        possAnswer.save()

        ####################################

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
        self.assertEquals("QCM", first_question.answerType.type)
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
        createUser("new user", "new.user@mail.com", "new password")

        users = getAllUsers()
        self.assertEquals(9, len(users))
        newUser = users[8]
        self.assertEquals("new user", newUser.login)
        self.assertEquals("new.user@mail.com", newUser.mail)
