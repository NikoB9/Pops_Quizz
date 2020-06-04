from Quizz.models import *
from django.contrib.auth import hashers

def set_db():
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

    gameStatusInProgress = GameStatus()
    gameStatusInProgress.type = "DRAFT"
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

    cat = Category()
    cat.label="Autre catégorie"
    cat.description="Qui possède des questions particulières"
    cat.save()

    f = Form()
    f.name = "Premier formulaire"
    f.description = "C'est parti !"
    f.author = userWawa
    f.is_public = True
    f.save()
    f.categories.add(cat)
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
    game.is_real_time=False
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
    f.categories.add(cat)
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
    f.is_public = False
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
