from django.db import models

class User(models.Model):
    login = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    

BEST_MEMBERS = [
    'Mr. Freeman',
    'Dr. House',
    'Bender',
    'Queen Victoria',
    'V. Pupkin'
]

POPULAR_TAGS = [
    'perl',
    'python',
    'TechnoPark',
    'MySQL',
    'django',
    'Mail.Ru',
    'Voloshin',
    'Firefox'
]

QUESTIONS = []
for id in range(80):
    ANSWERS = []
    for i in range(id * id):
        ANSWERS.append({
            'id': i,
            'text': f'Text of Answer {i}'
        })
    QUESTIONS.append({
        'id': id,
        'title': f'Question {id}',
        'text': f'Text of Question {id}',
        'answers_number': id * id,
        'answers': ANSWERS,
        'tags': [f'tag{i}' for i in range(id)]
    })

HOT_QUESTION_IDS = [0, 5, 12]

IS_AUTH = False

