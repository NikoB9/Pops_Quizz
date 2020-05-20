from Quizz.models import Form, Question, PossibleAnswer, AnswerType


f = Form()
f.name = "Premier formulaire"
f.description = "C'est parti !"
f.save()

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
f.save()

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
f.save()

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
f.save()

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
f.save()

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
f.save()

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
f.save()

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