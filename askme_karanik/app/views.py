from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(request):
    context = {'questions': models.QUESTIONS, 'isAuth': models.IS_AUTH}
    return render(request, 'index.html', context=context)

def question(request, question_id: int):
    if question_id < 0 or question_id >= len(models.QUESTIONS):
        return HttpResponse(status=404, content="Not Found")

    question_item = models.QUESTIONS[question_id]
    context = {'question': question_item, 'isAuth': models.IS_AUTH}
    return render(request, 'question.html', context=context)

def hot(request):
    questions = []
    for i in range(len(models.HOT_QUESTION_IDS)):
        for j in range(len(models.QUESTIONS)):
            if models.QUESTIONS[j]['id'] == models.HOT_QUESTION_IDS[i]:
                questions.append(models.QUESTIONS[models.HOT_QUESTION_IDS[i]])
                break
    
    context = {'questions': questions, 'isAuth': models.IS_AUTH}
    return render(request, 'hot.html', context=context)

def tag(request, tag_name: str):
    questions = []
    for i in range(len(models.QUESTIONS)):
        question = models.QUESTIONS[i]
        for j in range(len(question['tags'])):
            if question['tags'][j] == tag_name:
                questions.append(question)
                break

    context = {'questions': questions, 'tag_name': tag_name, 'isAuth': models.IS_AUTH}
    return render(request, 'tag.html', context=context)

def login(request):
    context = {'isAuth': models.IS_AUTH}
    return render(request, 'login.html', context=context)

def signup(request):
    context = {'isAuth': models.IS_AUTH}
    return render(request, 'signup.html', context=context)

def ask(request):
    context = {'isAuth': models.IS_AUTH}
    return render(request, 'ask.html', context=context)

def settings(request):
    context = {'isAuth': models.IS_AUTH}
    return render(request, 'settings.html', context=context)