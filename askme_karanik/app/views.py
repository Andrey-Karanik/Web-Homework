from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from . import models
from .models import User

def paginate(request, objects_list, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_num = request.GET.get('page')
    page_o = paginator.get_page(page_num)
    return paginator, page_o

def index(request):
    paginator, page_o = paginate(request, models.QUESTIONS, 30)
    context = {'paginator': paginator, 'page': page_o, 'questions': models.QUESTIONS, 'isAuth': models.IS_AUTH, 'popular_tags': models.POPULAR_TAGS, 'best_members': models.BEST_MEMBERS}
    return render(request, 'index.html', context=context)

def question(request, question_id: int):
    if question_id < 0 or question_id >= len(models.QUESTIONS):
        return HttpResponse(status=404, content="Not Found")

    question_item = models.QUESTIONS[question_id]
    paginator, page_o = paginate(request, question_item['answers'], 3)
    context = {'paginator': paginator, 'page': page_o, 'question': question_item, 'isAuth': models.IS_AUTH, 'popular_tags': models.POPULAR_TAGS, 'best_members': models.BEST_MEMBERS}
    return render(request, 'question.html', context=context)

def hot(request):
    questions = []
    for i in range(len(models.HOT_QUESTION_IDS)):
        for j in range(len(models.QUESTIONS)):
            if models.QUESTIONS[j]['id'] == models.HOT_QUESTION_IDS[i]:
                questions.append(models.QUESTIONS[models.HOT_QUESTION_IDS[i]])
                break
    paginator, page_o = paginate(request, questions, 30)
    context = {'paginator': paginator, 'page': page_o, 'questions': questions, 'isAuth': models.IS_AUTH, 'popular_tags': models.POPULAR_TAGS, 'best_members': models.BEST_MEMBERS}
    return render(request, 'hot.html', context=context)

def tag(request, tag_name: str):
    questions = []
    for i in range(len(models.QUESTIONS)):
        question = models.QUESTIONS[i]
        for j in range(len(question['tags'])):
            if question['tags'][j] == tag_name:
                questions.append(question)
                break

    paginator, page_o = paginate(request, questions, 30)
    context = {'paginator': paginator, 'page': page_o, 'questions': questions, 'tag_name': tag_name, 'isAuth': models.IS_AUTH, 'popular_tags': models.POPULAR_TAGS, 'best_members': models.BEST_MEMBERS}
    return render(request, 'tag.html', context=context)

def login(request):
    context = {'isAuth': models.IS_AUTH, 'popular_tags': models.POPULAR_TAGS, 'best_members': models.BEST_MEMBERS}
    return render(request, 'login.html', context=context)

def signup(request):
    context = {'isAuth': models.IS_AUTH, 'popular_tags': models.POPULAR_TAGS, 'best_members': models.BEST_MEMBERS}
    return render(request, 'signup.html', context=context)

def ask(request):
    context = {'isAuth': models.IS_AUTH, 'popular_tags': models.POPULAR_TAGS, 'best_members': models.BEST_MEMBERS}
    return render(request, 'ask.html', context=context)

def settings(request):
    context = {'isAuth': models.IS_AUTH, 'popular_tags': models.POPULAR_TAGS, 'best_members': models.BEST_MEMBERS}
    return render(request, 'settings.html', context=context)